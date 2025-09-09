# Network Analyzer
I've been wanting to make a network analyzer for a while. I decided to skip most of the hardware design by using a software defined radio and focus more on data processing.

## Theory of operation
A network analyzer excites a device under test (DUT) with a RF signal and measures the resulting reflected and transmitted signals at all other ports.
To do this, we must do more than simply measure node voltages at each port since that will not discriminate between the incident and reflected signals.

## Network cascades
There are a few libraries ([scikit-rf](http://scikit-rf.org/) comes to mind) which can de-embed s-parameter measurements using measured cable data. I could have easily used this but decided instead to build my own. The math is pretty straightforward and this allows me to build in some extra features like interpolation over power and temperature. 
Eventually I may extend these tools for AWR style tuning and optimization. I may run into performance issues in Python so it's important that I cache as many calculations as practical to reduce real time computation.

## Hardware
![Pluto SDR](https://www.analog.com/-/media/analog/en/evaluation-board-images/images/adalm-pluto-web.gif?la=en&h=500&thn=1&hash=ED6731D2CD753AB1EAB03823D56B039C)

The Pluto uses an AD9363 transceiver with Zynq XC7Z010 SoC. It runs Linux and can be accessed over USB, or in my case Ethernet through a USB-OTG adapter.

The original Pluto SDR only supported a single channel each of TX and RX which would work for my purposes with an external switching network.
I have a newer version of the Pluto which breaks out two channels each direction so I opted to eliminate switches and just use both channels. This works for a 2 port network analyzer but would be again require switches for more ports.


## User Interface
Since I would like to seamlessly use this network analyzer in automated tests along with my other lab equipment, I'm making all functions of the VNA accessible as a single Python class.

Calibration data can be saved as a few `Network` objects, one for each port, and passed to `NetworkAnalyzer` for de-embedding.

```Python
with NetworkAnalyzer(
    "192.168.2.1",
    power = -5, # dBm
    frequency = np.linspace(1e9, 3e9, 201), # Hz
    calibration = [
        Network("cable1.s2p"),
        Network("cable2.s2p"),
    ]
) as na:
    # measure and plot one sweep
    data = na.get_sweep()
    bh_networks.plot_logmag(data)
    plt.show()

    # start GUI to continuously measure
    na.start_gui()
```

This leaves the issue of how to generate accurate calibration data in the first place, and this is done with a calibrator object (`SOLT`, `TRL`, etc)

```Python
with NetworkAnalyzer(
    "192.168.2.1",
    power = -5, # dBm
    frequency = np.linspace(1e9, 3e9, 201), # Hz
    bandwidth = 5e3, # Hz
) as na:
    solt = Solt(na)
    
    # delays should be added for user to re-connect cables
    solt.measure("S", 1)
    solt.measure("O", 1)
    solt.measure("L", 1)
    solt.measure("S", 2)
    solt.measure("O", 2)
    solt.measure("L", 2)
    solt.measure("T", [1,2])

    calibration = solt.networks()
    na.calibration = calibration

    write_touchstone(calibration[0], "cable1.s2p")
    write_touchstone(calibration[1], "cable2.s2p")
```

The `SOLT` class assumes the ideal case of perfect short, open, load, and trough. If a more accurate calibration is desired with a known calibration kit:

```Python
class MyFancySolt(Solt):
    def __init__(self, *args, **kwargs):
        standards = {
            "S": Network("my_fancy_solt_s.s1p"),
            "O": Network("my_fancy_solt_o.s1p"),
            "L": Network("my_fancy_solt_l.s1p"),
            "T": Network("my_fancy_solt_t.s2p"),
        }
        super().__init__(standards=standards, *args, **kwargs)
```

Similarly, custom calibration kits can be specified with ideal components:
```Python
class MyFancyTrl(Trl):
    def __init__(self):
        standards = {
            "L": DelayLine(t = 28e-12), # 28ps delay
        }
        super().__init__(standards=standards, *args, **kwargs)
```

### GUI
I don't particularly enjoy spending a lot of time building GUIs so I opted to make this one pretty minimal.
Debugging of hardare is much easier when plots update in real time so I consider that to be a necessary feature. There are a few other controls that would be nice to be able to change on the fly, but I opted to keep it as simple as possible since this GUI is more a proof of concept than anything else. I can choose to add more complexity later if I feel limited by this one.

## Going further
There are a few ways I could see extending this project in the future.

I've gotten used to using an electronic calibrator (ECal) for network analyzers at work and the convenience is phenomenal. I would be able to make something similar without any significant software modifications by building a module with a few switches and known loads.

One which would be quite useful would be to bake in control of external switches and automatic replacement of calibration networks so this can be extended to arbitrarily many ports. As it stands this is already possible, just that the user must manage switch control and calibration.

Additionally, external frequency conversion could be very useful to measure at higher frequencies. 

Another area to improve is the GUI. I probably won't do this, at least in the near future, since I'm perfectly happy to write scripts for anything beyond than the capability of the current GUI.

At some point I would also like to build myself the hardware for a network analyzer rather than just using an SDR.
