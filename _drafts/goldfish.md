# High Power Rocket Ingiter
One day in college, I was faced with the question of how to best light a rocket from roughly a mile away. The simple response to this would be to run a pair of wires the entire distance, however this isn't an ideal solution since many high power rocketry (HPR) launches do not take place at permanent launch sites. There are many locations where model rockets and smaller HPR can be launched, however as rockets get bigger, launches must take place further from civilization. Another factor to deciding launch locations is retrieval. A flat plain devoid of shrubbery is in many ways ideal both for safety as well as simplifying retrieval after landing.

My solution was to make a wireless ignition system controlled by amateur radio.

## Goldfish
The original ignition system was made in one or two days in my dorm room on a breadboard using parts I had on hand.

Once everything was built, I wanted some form of enclosure so I could safely transport without risking inadvertant disconnection or shorting of wires. My roomate had just finished a box of goldfish, so I stole it and added some holes for external connectors.
The project got its nickname from this temporary enclosure.

## Goldfish 2
Nothing functionally changed in the 2nd revision. The only changes were to solder all circuitry on a perf-board and to replace the cardboard box with something a little more durable.

Goldfish 2 still lacked waterproofing but was a bit more tolerant of muddy conditions than a literal cardboard box.

## Goldfish 3
I knew from the start that requiring someone bring a laptop into potentially wet or muddy conditions wasn't ideal. It was however a very easy interface to build in an evening. Goldfish 3 was an attempt to improve the user interface, ruggedize, and protect against power transients.

Unlike the previous versions Goldfish 3 had an internal battery, ensuring a poor connection or light bump couldn't result in indeterminate output state. Additionally it added many redundant safety features both for protecting humans and internal electronics.

Goldfish 3 was used for far longer than the previous model but still experienced a few major issues: insufficient power and unreliable communication.

### Power Issues
Aside from some basic issues I fixed while bringing up the system, there were three noteworthy power related issues.

The first issue was that I half-assed the battery charger and as a result could never charge the internal battery without some disassembly. I wasn't certain what battery chemistry I wanted to use and knew it would be easy to upgrade the charger later, so I just threw in a half-baked design with the hope that I could get away with it.
While I would likely do the same thing again for a project intended only for myself, I've learned that this is actually quite a hassle since the hardware is used by others at CUSRL.
Particularly given some semi-delicate PCB fixes and the very tight fit in the enclosure, I didn't want anyone else removing and reinstalling the battery. This meant that extra coordination was required to make sure I personally got a chance to recharge the battery before each launch or motor static fire.

The next issue cropped up because of the lack of internal charging. My power circuit intentionally disconnected all loads except a single 100kΩ resistor when switched off to conserve power. If this were truly the only load, the battery would last for over two years in the off state. The parameter I failed to consider was battery self-discharge. This resulted in a battery life of less than a month.

The third issue was quite easy to fix but was an important lesson in the importance of accurate specifications. The output of Goldfish 3 had a series resistor to protect internal electronics from overcurrent in the case of a shorted output. I sized this resistor based on the current required to light some standard igniters. What I didn't know was that CUSRL intended to use a different igniter for the larger motors in development. These new igniters have a much higher internal resistance and did not reliably ignite with the available current. The solution was simply to reduce the current-limit resistor value from 3Ω to 1.5Ω resulted in many problems at the first test using the new igniter.

### Communication
Strangely enough, a VHF FM radio puchased more for its bottom-of-the-barrel price than any performance metrics doesn't necessarily perform very well.

I always intended to replace the radio with something custom but since we didn't have communication problems with Goldfish 2, I decided to postpone that change until a later upgrade. Unfortunately this module wasn't particularly consistent and with a sample size of 1 I didn't predict the magnitude of issues we would experience on version 3.
Receive sensitivity and transmit power of version 3 were significantly worse than I saw with version 2. This was never a safety issue since the system was designed around all potential faults (including communication issues) resulting in a safe failure state in which the output could not be activated.

## Goldfish 4
After more members of CUSRL realized the benefits of real time communication on the ground between humans and the launchpad, we decided to add a COTS wireless network. Goldfish can now piggyback off of this communication link rather than requiring its own internal radio.

I am also adding a proper battery managemnet (charging and balancing) system which will also have the benefit of reducing power sequencing complexity since it will include a battery disconnect feature enabling low-power standby mode.


## Going Further
I doubt that I will continue to improve this project beyond its current state.
