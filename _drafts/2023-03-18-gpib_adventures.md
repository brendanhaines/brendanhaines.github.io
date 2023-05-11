---
layout: post
title: "Adventures with GPIB"
date: 2019-05-05 23:00:00 -0600
categories: Testing
---

I've been trying to interface with GPIB instruments but struggling a lot with GPIB adapters. Hopefully this can be useful to someone else trying to automate old instruments.

I started out with a Agilent 82357B USB to GPIB adapter. I was able to get my power meter to respond to a GPIB query exactly *once* but never again. After fighting with `linux-gpib` configuration on and off for a few months, I got fed up and got an Agilent E5810A Ethernet to GPIB adapter. I had no problems communicating with my power meter immedately after power everything on.

<!--more-->

I'm using [PyVISA](https://pyvisa.readthedocs.io/en/master/) with the `pyvisa-py` backend. I've now begun writing python device drivers to simplify scripting this and other test equipment.

```python
import visa
rm = visa.ResourceManager('py')

ip = '169.254.58.10'
gpib_addr = 13
inst = rm.open_resource(f'TCPIP::{ip}::gpib0,{gpib_addr}::INSTR')
```
