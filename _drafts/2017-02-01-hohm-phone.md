---
layout: post
title: "Hohm Phone: Cell Phone for the Elderly"
date: 2017-01-30 19:00:00 -0700
categories: Projects
permalink: /:categories/:title/
---

# Intro
For my freshman projects class, we were prompted with using some aspect of touch tone phones in a new way. Ultimately, my group decided on making a cell phone targeted at the elderly population, some of whom struggle to use miniaturized cell phones or much more complicated smartphones.

**The primary goal of our project was to create a working cell phone with as similar an interface to old landlines as possible to simplify use.**

# Design
The design is based around an Arduino and inexpensive SIM800L GSM module. Schematic, board layout, and Arduino code are available in the [Git repository][repo]. As a brief overview, the ATMEGA328P (microcontroller that's on an Arduino Uno/Nano) communicates with the SIM800L by sending AT commands over UART and monitors the keypad for button presses. There is additionally a SIM card on the back of the board which interfaced directly with the SIM800L over SPI. Interpretation of phone numbers is performed on the ATMEGA328P and currently works for calls within the United States but would need significant improvement to be used for international calling.

To save space, in addition to it just being cool, I designed a PCB for the phone. 

![PCB Top][pcb-top] | ![PCB Bottom][pcb-bottom]

![Populated PCB][populated-pcb]

Through this process, I learned quite a bit about PCB design and debugging as well as how that can fit into a larger project's workflow. This is the largest and most complicated PCB I've made to date as well as the most difficult to solder package (LGA-88 with lots of heat dissipation).

Since I don't personally have any reflow soldering equipment, I had to use what was available in the circuits lab here at CU. Unfortunately, the PCB arrived during Thanksgiving break and I couldn't get access to those tools for a week, leaving me with just 1 week to populate, test, and debug the board. This ended up being pretty stressful. Population of the SIM800L module became a lot easier when I started using a hot air station powerful enough for the job as opposed to a hand held gun.



![Phone Internals][internals] | ![Initial Assembly][front-taped]

# Final Product
The finished phone is fully capable of placing and receiving calls within the country and maintains the same interface as old touch tone phones with the addition of an answer button (green) and moving the end button (on hook) from a base station to the handset (red).

![Final Phone][final-phone] | ![Final Phone][final-phone-separate]

![Final Phone Render][final-render] | ![Final Phone Render][final-render-docked] | ![Final Phone Render][final-render-bottom]


# Further Development
Throughout the design process, I came across a few additional feature that I would like to incorporate into the Hohm Phone (if there's a version 2). The most important feature is definitely functional charging since that didn't work and is very essential to being functional at all in the real world.

Second on the list is adding a voice changer to lower the pitch of incoming voices. I remember whenever my family would call my great grandmother, she would have no trouble hearing anything my dad said but struggled immensely with understanding anyone else because our voices were higher higher pitch. During this project, I came across a couple phone voice-changer projects which reminded me of these experiences and would be a great addition to a phone specifically made for the elderly.

# Resources
* Git Repository ([GitHub][repo])

[pcb-top]:{{site.url}}/assets/hohm-phone/IMG_board_top.png
[pcb-bottom]:{{site.url}}/assets/hohm-phone/IMG_board_bottom.png
[populated-pcb]: {{site.url}}/assets/hohm-phone/IMG_populated_pcb_cropped.jpg
[front-taped]: {{site.url}}/assets/hohm-phone/IMG_front.jpg
[internals]: {{site.url}}/assets/hohm-phone/IMG_guts_assembled.jpg
[charging]: {{site.url}}/assets/hohm-phone/IMG_charging.jpg

[final-phone]: {{site.url}}/assets/hohm-phone/IMG_final.jpg
[final-phone-separate]: {{site.url}}/assets/hohm-phone/IMG_final_separate.jpg

[final-render]: {{site.url}}/assets/hohm-phone/IMG_render_final_top.png
[final-render-docked]: {{site.url}}/assets/hohm-phone/IMG_render_final_docked.png
[final-render-bottom]: {{site.url}}/assets/hohm-phone/IMG_render_final_bottom.png

[repo]: https://github.com/brendanhaines/Hohm-Phone