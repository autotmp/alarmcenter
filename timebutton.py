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

## custom button that update time
class TimeButton(Button):
    markup = True

    def __update(self, dt):
        self.text = "[b]" + strftime('%H')
        self.text += strftime(':%M') + "[/b]"
        self.text += strftime(':%S')

    def __init__(self, **kwargs):
        super(Button,self).__init__(**kwargs)
        self.font_size = self.height/1.5
        Clock.schedule_interval(self.__update, 1.0)
