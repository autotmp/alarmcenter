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
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.spinner import Spinner

class AlarmWidget(BoxLayout):
    orientation = 'horizontal'

    def build_vbox(self):
        layout = BoxLayout(orientation='vertical')

    def __init__(self, text, **kwargs):
        super(AlarmWidget,self).__init__(**kwargs)

        self.hour = 12
        self.minute = 0
        self.text = text

        self.vbox = BoxLayout(orientation='vertical')

        self.alarm = Button(text=text, font_size=(self.height/3.0), markup='True')
        self.vbox.add_widget(self.alarm)

        self.add_widget(self.vbox)
