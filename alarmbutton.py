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
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.gridlayout import GridLayout
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

    def build_set_alarm(self):
        layout = BoxLayout(orientation='horizontal')

        hspin = Spinner(text=str(self.hour), values=list(map(str, list(range(1, 25)))))
        hspin.bind(text=self.set_hour)
        mspin = Spinner(text=str(self.minute), values=list(map(str, list(range(1, 60)))))
        mspin.bind(text=self.set_minute)

        enable = ToggleButton(text='Enabled', state=self.enabled, size_hint=(0.3, 1.0))
        enable.bind(state=self.toggle_alarm)

        layout.add_widget(hspin)
        layout.add_widget(mspin)
        layout.add_widget(enable)

        return layout

    def set_hour(self, instance, value):
        print('hour = ', self.hour)
        self.hour = value

    def set_minute(self, instance, value):
        print('minute = ', self.minute)
        self.minute = value

    def toggle_alarm(self, instance, value):
        print("toggle alarm", value)
        self.enabled = value

    def update_alarm(self):
        print("popup dismissed")

    def launch_popup(self):
        layout = self.build_set_alarm()
        title = 'Set ' + self.text
        popup = Popup(title=title, content=layout, size_hint=(0.7, 0.2))
        popup.bind(on_dimiss=self.update_alarm)
        popup.open()

    def on_press(self):
        print("AlarmButton pressed")
        self.launch_popup()

    def __init__(self, **kwargs):
        super(Button,self).__init__(**kwargs)
        Window.allow_vkeyboard = True
        self.font_size = self.height/3.0
        self.hour = 12
        self.minute = 0
        self.enabled = 'normal'
