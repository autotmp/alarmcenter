# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

## python imports
import datetime
import time
from time import strftime
import sched
from apscheduler.schedulers.background import BackgroundScheduler

import kivy
kivy.require('1.10.0')

## kivy imports
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.logger import Logger
from kivy.core.audio import SoundLoader

class SpinnerButton(SpinnerOption):
    def __init__(self, text, **kwargs):
        super(SpinnerOption, self).__init__()
        self.font_size = self.height
        self.text = text

class AlarmWidget(BoxLayout):
    orientation = 'horizontal'
    hour = 12
    minutes = 0

    def build_alarm_popup(self):
        layout = BoxLayout(orientation='horizontal')

        hourspin = Spinner(text=str(self.hour), 
                           values=list(map(str, list(range(1, 25)))), 
                           sync_height=True, 
                           font_size=(self.height/4.0), 
                           option_cls=SpinnerButton)

        hourspin.bind(text=self.set_hour)

        minspin = Spinner(text=str(self.minutes), 
                          values=list(map(str, list(range(1, 60)))), 
                          sync_height=True, 
                          font_size=(self.height/4.0), 
                          option_cls=SpinnerButton)

        minspin.bind(text=self.set_minute)

        layout.add_widget(hourspin)
        layout.add_widget(minspin)

        return layout

    def set_hour(self, instance, value):
        self.hour = value

    def set_minute(self, instance, value):
        self.minutes = value

    def launch_alarm_popup(self, instance):
        widget = self.build_alarm_popup()
        title = 'Set ' + self.name
        popup = Popup(title=title, content=widget, size_hint=(0.7, 0.3), 
            pos_hint={'y' : 35.0 / Window.height})
        popup.bind(on_dismiss=self.update_alarm)
        popup.open()

    def build_toggle_button(self):
        button = ToggleButton(text=self.text, font_size=(self.height/1.5), markup='True', size_hint=(1.0, 1.0))
        button.bind(state=self.toggle_alarm)
        return button

    def build_config_button(self):
        # ⚙
        button = Button(size_hint=(0.2,1.0), text=chr(2699))
        button.bind(on_press=self.launch_alarm_popup)
        return button

    def wakeup(self):
        print("get up " + self.name)

        sound = SoundLoader.load('annoying-sound.wav')

        if sound:
            sound.loop = True
            sound.play()

    def update_alarm(self, instance):
        # update the displayed time
        alarm = datetime.time(int(self.hour), int(self.minutes))
        self.alarm.text = "[b]" + alarm.strftime('%H:%M') + "[/b]"

        # check the alarm is currently on, if enabled (`down`) then remove the
        # current job and schedule a new one
        if self.enable.state == 'down':
            self.scheduler.reschedule_job(self.name, trigger='cron', hour=int(self.hour), minute=(self.minutes), day_of_week="mon-sun")

    def toggle_alarm(self, instance, value):
        if value == 'down':
            self.scheduler.add_job(self.wakeup, 'cron', hour=int(self.hour), minute=(self.minutes), day_of_week="mon-sun", id=self.name)
        else:
            self.scheduler.remove_job(self.name)

    # def on_stop(self):
    #     print("AlarmWidget " + self.name + "stopping operations")
    #     self.scheduler.remove_job(self.name)

    def __init__(self, name, **kwargs):
        super(AlarmWidget,self).__init__(**kwargs)

        self.name = name

        # set initial display
        alarm = datetime.time(int(self.hour), int(self.minutes))
        self.text = "[b]" + alarm.strftime('%H:%M') + "[/b]"

        # create and start scheduler
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

        # create widgets and dadd to layout
        self.alarm = self.build_toggle_button()
        self.enable = self.build_config_button()
        self.add_widget(self.alarm)
        self.add_widget(self.enable)
