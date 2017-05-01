---
layout: post
title: "Hohm Phone: Cell Phone for the Elderly"
date: 2017-05-01 00:00:00 -0600
categories: Projects
permalink: /:categories/:title/
---

# Intro
For my freshman projects class in the Fall of 2016, we were prompted with using some aspect of touch tone phones in a new way. Ultimately, my group decided on making a cell phone targeted at the elderly population, some of whom struggle to use miniaturized cell phones or much more complicated smartphones.

**The primary goal of our project was to create a working cell phone with as similar an interface to old landlines as possible to simplify use.**

# Design
The design is based around an Arduino and inexpensive SIM800L GSM module. Schematic, board layout, and Arduino code are available in the [Git repository][github-repo]. As a brief overview, the ATMEGA328P (microcontroller that's on an Arduino Uno/Nano) communicates with the SIM800L by sending AT commands over UART and monitors the keypad for button presses. There is additionally a SIM card on the back of the board which interfaced directly with the SIM800L over SPI. Interpretation of phone numbers is performed on the ATMEGA328P and currently works for calls within the United States but would need significant improvement to be used for international calling.

To save space, in addition to it just being cool, I designed a PCB for the phone. 

![PCB Top][pcb-top] | ![PCB Bottom][pcb-bottom]

![Populated PCB][populated-pcb]

Through this process, I learned quite a bit about PCB design and debugging as well as how that can fit into a larger project's workflow. This is the largest and most complicated PCB I've made to date as well as the most difficult to solder package (LGA-88 with lots of heat dissipation).

Since I don't personally have any reflow soldering equipment, I had to use what was available in the circuits lab here at CU. Unfortunately, the PCB arrived during Thanksgiving break and I couldn't get access to those tools for a week, leaving me with just 1 week to populate, test, and debug the board. This ended up being pretty stressful. Population of the SIM800L module became a lot easier when I started using a hot air station powerful enough for the job as opposed to a hand held air gun.

Once populated, testing was fairly straightforward and showed only a few issues:
* Indicator LEDs (low battery, no service) wouldn't light
* Speaker volume very low
* Battery would not charge

Unfortunately, due to the time crunch before the design expo, we abandoned charging with our fallback plan of removing the battery and charging it on a separate lipo charger. This worked both for testing and demonstration and 

![Phone Internals][internals] | ![Initial Assembly][front-taped]

# Final Product
The finished phone is fully capable of placing and receiving calls within the country and maintains the same interface as old touch tone phones with the addition of an answer button (green) and moving the end-call button from a base station to the handset (red).

![Final Phone][final-phone] | ![Final Phone][final-phone-separate]

![Final Phone Render][final-render] | ![Final Phone Render][final-render-docked] | ![Final Phone Render][final-render-bottom]


# Further Development
Throughout the design process, I came across a few additional features that I would like to incorporate into the Hohm Phone (if there ever is a version 2). The most important feature is definitely to fix charging since that didn't work and is very essential to being functional at all in the real world. Additionally, improving audio volume would be important.

Next on the list is adding a voice changer to lower the pitch of incoming voices. I remember whenever my family would call my great grandmother, she would have no trouble hearing anything my dad said but struggled to understand anyone else because our voices were higher pitched. During this project, I came across a couple voice-changer projects which reminded me of these experiences and would be a great internal addition to a phone specifically made for the elderly.

# Resources
* Git Repository ([GitHub][github-repo])

[pcb-top]:{{site.baseurl}}/assets/hohm-phone/IMG_board_top.png
[pcb-bottom]:{{site.baseurl}}/assets/hohm-phone/IMG_board_bottom.png
[populated-pcb]: {{site.baseurl}}/assets/hohm-phone/IMG_populated_pcb_cropped.jpg
[front-taped]: {{site.baseurl}}/assets/hohm-phone/IMG_front.jpg
[internals]: {{site.baseurl}}/assets/hohm-phone/IMG_guts_assembled_small.jpg
[charging]: {{site.baseurl}}/assets/hohm-phone/IMG_charging.jpg

[final-phone]: {{site.baseurl}}/assets/hohm-phone/IMG_final.jpg
[final-phone-separate]: {{site.baseurl}}/assets/hohm-phone/IMG_final_separate.jpg

[final-render]: {{site.baseurl}}/assets/hohm-phone/IMG_render_final_top.png
[final-render-docked]: {{site.baseurl}}/assets/hohm-phone/IMG_render_final_docked.png
[final-render-bottom]: {{site.baseurl}}/assets/hohm-phone/IMG_render_final_bottom.png

[github-repo]: https://github.com/brendanhaines/Hohm-Phone
