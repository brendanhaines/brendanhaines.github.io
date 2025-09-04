---
layout: post
title: "Lab Equipment Project Intro"
date: 2019-05-05 22:00:00 -0600
categories: Projects Tools
---

The purpose of this post is to outline scope and architecture of an extraordinarily large project I'm strarting. I've begun the process of building myself an electronics lab, and when I say building I mean designing from the ground up.

Some of the gear I intend to build includes:

- Oscilloscope
- Arbitrary waveform generator
- Power Supply
- RF signal generator
- Spectrum analyzer
- VNA
- Power meter

<!--more-->

While I fully intend to build all of these, I won't be done for years so I'll still be interspersing this with other, smaller projects.

Architecturally, these devices will interface with Ethernet and implement the VISA standard. I've considered fully implementing LXI though I probably won't since it would require significantly more time and effort.
Mechanically, I'd like everything to be mounted in a server rack and well integrated. Since I won't need anywhere near a 1U volume to implement any of these devices, I'll be making everything fit as modules into a backplane (similarly to blade style servers) and integrate precise timing into that backplane. Additionally, there will be a separate device with buttons, knobs, and a high resolution display in front of a linux computer to make the user interface as similar to ordinary lab equipment as possible.

## Progress

I've started working on hardware interfacing and have been building up a set of hardware, firmware, and software libraries which can be shared across many of these devices. Some communication achievements I've reached include microcontrollers responding to pings over Ethernet and a working pair of C and Python libraries which enable packetized UART communication.

To enable work on the user interface to get going, I've tried to drive the screen from an iPad 3 from HDMI though I missed a few lines in the HDMI &rarr; DisplayPort converter's datasheet which state that it doesn't work at this display's particular resolution. I've changed my approach and will likely be integrating an AMD SOM which can natively drive a displayport display directly into the human interface box.

