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
from kivy.logger import Logger

## custom button that displays current time
class TimeButton(Button):
    markup = True

    def _update(self, dt):
        self.text = "[b]" + strftime('%H')
        self.text += strftime(':%M') + "[/b]"
        self.text += strftime(':%S')

    def __init__(self, **kwargs):
        super(Button,self).__init__(**kwargs)
        self.font_size = self.height/1.5
        self.event = Clock.schedule_interval(self._update, 1.0)
        Logger.info('TimeButton Clock.schedule_interval for 1.0')
