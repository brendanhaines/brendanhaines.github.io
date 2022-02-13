---
layout: post
title: "GPIB Issues"
date: 2019-05-05 23:00:00 -0600
categories: Equipment
permalink: /:categories/:title/
---

I've been trying to interface with GPIB instruments but struggling a lot with GPIB adapters. Hopefully this can be useful to someone else trying to automate old instruments.

I started out with a Agilent 82357B USB &rarr; GPIB adapter. I was able to get my power meter to respond to a GPIB query *once* but never again. After fighting with `linux-gpib` configuration on and off for a few months, I got fed up and got an Agilent E5810A Ethernet &rarr; GPIB adapter. Despite authentication issues on the university network, I had no problems communicating with my power meter no more than an hour after power everything on.

<!--more-->

I'm using [PyVISA](https://pyvisa.readthedocs.io/en/master/) with the `pyvisa-py` backend. I've now begun writing python device drivers to simplify usage of the meter.

```python
import visa
rm = visa.ResourceManager('py')

ip = '169.254.58.10'
gpib_addr = 13
inst = rm.open_resource(f'TCPIP::{ip}::gpib0,{gpib_addr}::INSTR')
```

The IP address `169.254.58.10` is the default IP if no DHCP server is found.