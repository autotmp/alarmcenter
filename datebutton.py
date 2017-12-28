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

## custom button that displays the current date
class DateButton(Button):
    markup = True

    def _update(self, dt):
        self.text = strftime('[b]%a[/b] %b %d %Y')

    def __init__(self, **kwargs):
        super(DateButton,self).__init__(**kwargs)
        self.font_size = self.height/1.5
        Clock.schedule_interval(self._update, 1.0)
        Logger.info('DateButton Clock.schedule_interval for 1.0')
