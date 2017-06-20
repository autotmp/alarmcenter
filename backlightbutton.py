# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

## python imports

import kivy
kivy.require('1.10.0')

## kivy imports
from kivy.uix.button import Button

## custom button that turns the backlight on/off
class BacklightButton(Button):
    markup = True

    def __init__(self, **kwargs):
        super(BacklightButton,self).__init__(**kwargs)
        self.text = "Backlight [b]Off[/b]"
        self.font_size = self.height/3.0
