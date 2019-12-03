## What is this? its LTunes ofc
We designed and created this project for our senior design class at 🤙UTA🤙. This project is a Laser harp that is controlled by a [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) which controls the display and sound creation, and is supported by a [Teensy 3.6](https://www.pjrc.com/store/teensy36.html) micro-controller which encodes midi signals for the raspberry pi to process.

## Dependencies
### Raspbian OS
To install dependencies on your raspberry pi run the following command in your terminal
- `sudo apt-get install -y fluidsynth alsa python3 python3-pip`


### Anything else
This project depends on a [Fluidsynth](http://www.fluidsynth.org/) to process the [MIDI](https://en.wikipedia.org/wiki/MIDI) signals and processing them in the [SoundFont](https://en.wikipedia.org/wiki/SoundFont) files. 
The GUI and server processing was coded in [python 3.6.0](https://www.python.org/downloads/). 

## Setting up environment
- Clone this repository onto your Raspberry Pi 4
	- `git clone https://github.com/rtorres678/Senior-Design-Project.git`
- [Load](https://www.dummies.com/computers/arduino/how-to-upload-a-sketch-to-an-arduino/) the code in `src/teensy_code/prototype-6.ino` into the teensy micro controller.
	- You can load this using the [Arduino IDE](https://www.arduino.cc/en/main/software)
## Running the program

**Manual** 
- From your Home directory run
	- `sh Senior-Design-Project/src/pi_code/startup_script.sh`

**Boot From Startup**
- `nano ~/.config/lxsession/LXDE-pi/autostart` 
- append `@sh ~/Senior-Design-Project/src/pi_code/startup_script`
