---
layout: post
title: "Wireless Rocket Igniter: Goldfish2"
date: 2019-05-05 12:00:00 -0600
categories: Projects
permalink: /:categories/:title/
---

As a project sponsored by CU's rocketry club, COBRA (now [CUSRL](https://www.colorado.edu/studentgroups/cobra/)), I've been developing a wireless ignition system for high power rockets. When we're launching to over ten thousand feet, rockets get large enough that we need thousands of feet between ourselves and the launchpad. Rather than carry a spool of wire large enough to span that safety distance, we decided to look into wireless ignition systems.

![Goldfish2][goldfish2_front]

<!--more-->

*Note that we are not in any way sponsored by Pepperidge Farm.*

## Design Requirements

- The system must be safe and never fire unless commanded.
- It must be reliable and always fire when commanded, or if unable to fire must make the operator aware of such failure.
- It must be simple enough that someone without experience can safely operate it.
- It should be legal to operate with no more than a technician class amateur radio license.

***Be aware that this is not a finished product. Don't blindly copy this project. You take full responsibility for everything you make. Please don't blow yourself up.***

Mainly for the sake of licensing, I've chosen to use the 130MHz/433MHz Ham radio bands for all communications. This allows for transmissions of several Watts for decent range and ensuring a multitude of handheld transceivers to use for one end of the link. I've chosen to use DTMF tones for authentication and launch codes since they can be easily supported both by handheld transceivers as well as dedicated decoding hardware.

**IMAGE OF SCHEMATIC??**

<!-- The most important requirement is to make something safe which minimizes the possibility for accidental firing as well as misfires. While it is obvious why an early or accidental ignition could have catastrophic consequences, it may be less obvious why a misfire, or dud, could be nearly as bad. In the situation where a rocket is expected to fire but does not ignite, the dangerous situation arises where a person must approach the rocket while it is in an unknown state and has the possibility of catastrophic failure.

One of most foreign requirements for me on this project is the need to make this system entirely stupid-proof. I usually am only anticipating myself using the tools I make but in this case I have to plan ahead for others. It is quite likely that people who know nothing about the inner functioning of this system will have to operate it and be safe in doing so. -->

## Testing

I've probably tested the radio portion of this ingiter close to a hundred times over the course of firmware development. The high current portion has had fewer tests, however I've proven that it can repeatably supply **a few - NUMBER** amps (my power resistor can't handle much more) without disrupting system functionality. I've additionally fired around a dozen live igniters to ensure that pyro manufacturing variations don't negatively impact functionality.

Maybe a video...

## Future Plans

Though Goldfish2 is sufficient for some launch operations, it is not as robust and foolproof as I would like. I will be making a third version of this project with additional failsafes and physically tougher construction.

One of my biggest complaints with the current system is that the operator must carry around a laptop computer just to configure a few values before launch. This shouldn't be necessary and can be easily remedied with a keypad and alpha-numeric display.

[goldfish2_front]: {{base-url}}/assets/goldfish2/IMG_7899_CR2_embedded.jpg