# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

## python imports
import datetime
import time
from time import strftime
import sched

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

    def build_alarm_popup(self):
        layout = BoxLayout(orientation='horizontal')

        hspin = Spinner(text=str(self.hour), values=list(map(str, list(range(1, 25)))))
        hspin.bind(text=self.set_hour)
        mspin = Spinner(text=str(self.minute), values=list(map(str, list(range(1, 60)))))
        mspin.bind(text=self.set_minute)

        layout.add_widget(hspin)
        layout.add_widget(mspin)

        return layout

    def set_hour(self, instance, value):
        print('hour = ', self.hour)
        self.hour = value

    def set_minute(self, instance, value):
        print('minute = ', self.minute)
        self.minute = value

    def launch_alarm_popup(self, instance):
        widget = self.build_alarm_popup()
        title = 'Set ' + self.text
        popup = Popup(title=title, content=widget, size_hint=(0.7, 0.2))
        popup.bind(on_dismiss=self.update_alarm)
        popup.open()

    def build_alarm_button(self):
        button = Button(text=self.text, font_size=(self.height/3.0), markup='True', size_hint=(1.0,1.0))
        button.bind(on_press=self.launch_alarm_popup)
        return button

    def build_enable_button(self):
        button = ToggleButton(size_hint=(0.3,1.0))
        button.bind(state=self.toggle_alarm)
        return button

    def get_up(self):
        print("get up")

    def update_alarm(self, instance):
        print("popup dismissed")
        alarm = datetime.time(int(self.hour), int(self.minute))
        self.alarm.text = "[b]" + alarm.strftime('%H:%M') + "[/b]"
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enterabs(alarm, 1, self.get_up, ())
        print(alarm)

    def toggle_alarm(self, instance, value):
        print("toggle alarm", value)

    def __init__(self, text, **kwargs):
        super(AlarmWidget,self).__init__(**kwargs)

        self.hour = 12
        self.minute = 0
        self.text = text

        self.alarm = self.build_alarm_button()
        self.enable = self.build_enable_button()

        self.add_widget(self.alarm)
        self.add_widget(self.enable)
