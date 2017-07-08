# AlarmCenter
**AlarmCenter** is designed for use on a Raspberry Pi v3 + Official Raspberry Pi Touchscreen. Other installations are possible but not currently supported.

# Requirements
The following packages are required to execute, any derived requirements are not listed.
* Python 3.4+
* Kivy 1.10+ (via pip3)
* APScheduler (via pip3)
* urllib3 (via pip3)

# Installing Kivy
Kivy + Python3 is used for this project. The instructions below will install all required software to *develop* -- not just run. Packaging at a later date...

## OS X
Initial development environment. Assume that **Homebrew** is installed on the target system. The [installation instructions on the official Kivy](https://kivy.org/docs/installation/installation-osx.html) site are pretty close to the pin. Let's get the environment ready for Kivy.

```bash
$ brew install python3 pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
```

## Raspberry Pi (Raspbain OS)
Thankfully we've got a proper package manager in this environment. Just a few `apt-get` calls and we're in good shape. Once again the [installation instructions on the Kivy](https://kivy.org/docs/installation/installation-rpi.html) site get us most of the way there. The only modification is the installation of `python3` thrown into the mix. Maybe there are a few packages we don't need?

```bash
$ sudo apt-get update
$ sudo apt-get python3
$ sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip
```

## Installing Kivy and Support Libraries
Assuming we've got the house all setup, we can install Kivy and the other libraries used in the project.

Installing Kivy
```bash
$ pip3 install cython kivy
```

Installing additional libraries
```bash
$ pip3 install apscheduler urllib3
```

# Running **AlarmCenter**
For now packaging isn't a concern so a local Kivy install (global or virtual) is required. Clone and go

```bash
python3 alarmcenter.py
```
