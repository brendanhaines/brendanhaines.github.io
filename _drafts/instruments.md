# Lab Automation
Unlike college labs when we would manually record a few electrical measurements of a circuit, I've gotten used to a more automated workflow often used in industry and have written my own test automation libraries in Python.

The main purpose of this library is to automate extensive device characterization. I can simply set parameters in nested for loops to see performance over supply voltage, input power, bias current, frequency, time, etc.

I've also used this library to combine several tools to approximate another tool I lacked at the time. For instance, a few years ago, I wanted to measure antenna VSWR and was able to cable an synthesizer and two power detectors together with directional couplers to create a very slow, 1 port, scalar network analyzer. While this was a horrible tool to use and lacked decent calibration, it allowed me to quickly evaluate an antenna on short notice without needing access to a proper RF lab.

## VISA
Most lab equipment can be controlled with VISA (Virtual Instrument Software Architecture) commands. This is true of modern tools which connect over Ethernet as well as older GPIB devices.

I acquired an Agilent [E5810A](https://www.keysight.com/us/en/product/E5810A/langpib-gateway.html) Ethernet to GPIB gateway to enable communication with my older spectrum analyzer as well as any other used equipment I get in the future.

## Portability
One important requirement for me is that modifying a script to use slightly different (but similarly functioning) should be trivially easy. 

VISA instruments typically rely on LabView and proprietary DLLs to standardize generic instruments.

### pyvisa
[pyvisa] is a Python library for control of VISA instruments through a platform independant interface and can use a pure-python backend (pyvisa-py).
String descriptors of how to access an instrument are standardized regardless of communication media, for example:
- `tcpip:10.0.0.4:instr` - native Ethernet
- `tcpip:10.0.0.3:gpib0,13:instr` - GPIB address 13 through Ethernet gateway
- `usb:something:instr` - native USB
- `serial:/dev/ttyUSB0:instr` - Serial through USB adapter

One detriment of using pyvisa is that generic interfaces defined by DLLs are not used, so the user is responsible for composing [SCPI](https://en.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments) commands and parsing their responses.

### Automatic subclasses

```Python
HP8563e("tcpip:10.0.0.3:gpib0,13:instr") # works normally
SpectrumAnalyzer("tcpip:10.0.0.3:gpib0,13:instr") # returns a HP8563e object
Instrument("tcpip:10.0.0.3:gpib0,13:instr") # returns a HP8563e object
```

This allows for tests to be written with absolutely no consideration to the particular equipment which will be used for the test.

Of course a subclass can implement functions not available to the superclass for special features, however this allows for generic tests to be written once and ignored thereafter.