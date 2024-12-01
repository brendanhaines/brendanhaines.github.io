---
layout: post
title: "Adventures with GPIB"
date: 2024-12-01 16:00:00 -0600
categories: Testing
---

I needed to automate some old GPIB instruments but ran into issues with GPIB adapters. This post mostly serves to document the modifications I made and as a reference for the python command to connect.

<!--more-->

I started out with a (knockoff) Agilent 82357B USB to GPIB adapter. I was able to get my power meter to respond to a GPIB query exactly *once* but never again. After fighting with `linux-gpib` configuration on and off, I got fed up and bought an Agilent E5810A Ethernet to GPIB adapter. I had no problems communicating with my power meter immedately after power everything on.

I'm using [PyVISA](https://pyvisa.readthedocs.io/en/master/) with the `pyvisa-py` backend. I've now begun writing python device drivers to simplify scripting this and other test equipment.

```python
import visa
rm = visa.ResourceManager('py')

ip = '169.254.58.10'
gpib_addr = 13
inst = rm.open_resource(f'TCPIP::{ip}::gpib0,{gpib_addr}::INSTR')
```

## Backlight

Since this originally lived in my bedroom back in college I wanted to disable the backlight which is always on.
This is extremely easy by removing (or disconnecting one end of) two unlabeled resistors next to P102:

![Adapter Internals][e5810a_internals] | ![PCB Modification][e5810a_pcb]

[e5810a_internals]:{{site.baseurl}}/assets/gpib-adapter/e5810a_internals.jpg
[e5810a_pcb]:{{site.baseurl}}/assets/gpib-adapter/e5810a_pcb.jpg