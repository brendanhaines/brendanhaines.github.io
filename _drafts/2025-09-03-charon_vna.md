---
layout: post
title: "Charon: Vector Network Analyzer"
date: 2025-09-03 16:30:00 -0600
categories: Projects Tools
---

Have you ever wanted an RF network analyzer only to realize they cost tens of thousands of dollars?
I've been lucky enough to have access to a well equipped lab at work that I can use for my own projects.

<!--more-->

## Motiviation
Throughout both college and the start of my career I've met a lot of people who view electrical engineering as magic, and among electrical engineers many seem to view RF the same way.
It certainly requires some different considerations than many other areas of EE but I think there's nothing inherently unapproachable about the subject.
In the interest of improving accessibility of RF, I have a few projects in the works.

## Constraints
Since I'm trying to make tooling more accessible to students, hobbyists, and anyone wanting to learn about RF on the side, cost is a major constraint.
I don't have a specific budget for this but am certainly trying to minimize required expenses.

There is always a time and place for turning knobs by hand, but I've adopted a very human-out-of-the-loop philosophy regarding testing.
For this reason I consider a scriptable interface a necessity for pretty much any test equipment.

Most of the low-cost VNAs available today are only 1 or 1.5 ports (S11 and S21 but not S22 or S12).

## The Competition
There are several low-cost VNAs available today:
- [NanoVNA](https://nanovna.com/)
  - Cheap (<$200) and widely available
  - A few options in the range of 10kHz-3GHz
- [Pluto Network Analyzer](https://github.com/fromconcepttocircuit/pluto-network-analyzer)
  - Seems like a similar set of objectives to my project but more focused on cost and less on extensibility
- [LibreVNA](https://github.com/jankae/LibreVNA)
  - Checks most of the boxes for me

## Hardware
I've designed this VNA to be usable in a few configurations.
The simplest option is as a single port (S11 only) VNA.
This only requires a Pluto SDR and a bidirectional coupler (or better two couplers).

The Pluto SDR has some GPIOs which can control a few RF switches to make an N-port VNA. That requires:
- Pluto SDR
- 3 identical N-port (reflectionless) RF switches
- N bidirectional couplers

### Calibration Standards
A real calibration standard from Keysight will run a few thousand dollars. Given the target audience that's a non-starter.
My solution is to make a basic cal kit from a few spare SMA connectors.

Short | Open | Load | Thru
---|---|---|---
S | O | L | T

## Software


## Resources
- [PyPi](https://pypi.org/project/charon-vna)
- [Repository](https://git.brendanhaines.com/brendanhaines/charon_vna)
