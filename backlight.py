# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

## python imports
from pathlib import Path

bl_power = "/sys/class/backlight/rpi_backlight/bl_power"

def backlight_on():
    print("Backlight ON")

    if Path(bl_power).exists():
         with open(bl_power, "w") as text_file:
            text_file.write("0")

def backlight_off():
    print("Backlight OFF")

    if Path(bl_power).exists():
         with open(bl_power, "w") as text_file:
            text_file.write("1")