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
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.spinner import Spinner

Config.set('kivy', 'keyboard_mode', 'dock')
Config.set('kivy', 'keyboard_layout', 'numeric.json')

## custom button that turns the backlight on/off
class AlarmButton(Button):
    markup = True

    def on_press(self):
        print("AlarmButton pressed")

        popup = Popup(title='Test popup',
        content=Label(text='Hello world'),
        size_hint=(None, None), size=(400, 400))
        popup.open()

    def __init__(self, **kwargs):
        super(Button,self).__init__(**kwargs)
        Window.allow_vkeyboard = True
        self.font_size = self.height/3.0
