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
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
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
        layout = GridLayout(cols=2, rows=2, size_hint=(1.0,1.0))

        hspin = Spinner(text='6', values=list(map(str, list(range(1, 25)))))
        hspin.bind(text=self.set_hour)
        mspin = Spinner(text='0', values=list(map(str, list(range(1, 60)))))
        mspin.bind(text=self.set_minute)

        enable = ToggleButton(text='Enabled')
        enable.bind(state=self.toggle_alarm)

        done = Button(text='Done')
        #done.bind(on_release=self.close_alarm)

        layout.add_widget(hspin)
        layout.add_widget(mspin)
        layout.add_widget(enable)
        layout.add_widget(done)

        return layout

    def set_hour(self, instance, value):
        print('hour = ', self.hour)
        self.hour = value

    def set_minute(self, instance, value):
        print('minute = ', self.minute)
        self.minute = value

    def toggle_alarm(self, instance, value):
        print("toggle alarm", value)
        if value == 'down':
            self.alarm_enabled = True
        else:
            self.alarm_enabled = False

    def launch_popup(self):
        layout = self.build_set_alarm()
        popup = Popup(title='Set Alarm', content=layout, size_hint=(0.5, 0.5))
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
        self.enabled = False
