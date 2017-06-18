# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

## python imports
import datetime
import time
from time import strftime

import kivy
kivy.require('1.10.0')

## kivy imports
from kivy.uix.button import Button
from kivy.clock import Clock

## custom button that turns the backlight on/off
class BacklightButton(Button):
    markup = True

    def __init__(self, **kwargs):
        super(Button,self).__init__(**kwargs)
        self.text = "Backlight [b]Off[/b]"
        self.font_size = self.height/3.0
