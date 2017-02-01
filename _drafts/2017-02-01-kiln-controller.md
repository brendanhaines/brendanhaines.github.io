---
layout: post
title: "Wireless Kiln Controller: Part 1"
date: 2017-01-30 19:00:00 -0700
categories: Projects
permalink: /:categories/:title/
---

# Disclaimer
Kilns are very hot and can be dangerous. Don't be an idiot and if you don't know exactly what you're doing, check with someone who does before you get hurt. **I will not be held liable for any damages resulting from use of the information present on this page.**

# Intro
In 2012, there was a 500-1000 year flood in Boulder which caused a lot of damage, including destroying the temperature control on an old kiln in my basement. The purpose of this project is to make a replacement controller which ultimately could be networked using a house wifi network and possibly even be accessed from WAN. WAN access is stupid because of the fire risk of running a kiln when nobody is present, but it could be an interesting problem so I may look at that in the future.

Part 1 of this project involves the hardware and basic code to allow for manually turning on and off the kiln heating elements and measuring temperature.  
Part 2 will be better temperature control using the hardware from part 1.

# Design
The kiln controller is based on the ESP8266. This is a wifi capable microcontroller which conveniently can be programmed with Arduino.

# Temperature Sensing

# Load Switching

# Future Development

# References
* Git Repository ([GitHub][github-repo])
