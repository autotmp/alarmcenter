# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

## python imports
# import datetime
# import time
# from time import strftime
# from functools import partial

import kivy
kivy.require('1.10.0')

## kivy imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
# from kivy.config import Config
# from kivy.clock import Clock
# from kivy.properties import StringProperty, NumericProperty, ObjectProperty, BooleanProperty
# from kivy.uix.textinput import TextInput
# from kivy.core.window import Window
# from kivy.uix.vkeyboard import VKeyboard
# from kivy.uix.spinner import Spinner

## custom imports
from timebutton import TimeButton
from datebutton import DateButton
from backlightbutton import BacklightButton
from alarmbutton import AlarmButton
from alarmwidget import AlarmWidget

# launch as fullscreen application
# Config.set('graphics', 'fullscreen', 'auto')
# Config.set('kivy', 'keyboard_mode', 'dock')
# Config.set('kivy', 'keyboard_layout', 'numeric.json')

# main
class AlarmCenterApp(App):

    def if_root(self):
        print("i am root")

    def build_left(self):
        # create left column
        layout = BoxLayout(orientation='vertical')

        timebutton = TimeButton(text='Time', size_hint=(1.0, 1.0))
        layout.add_widget(timebutton)

        datebutton = DateButton(text='Date', size_hint=(1.0, 1.0))
        layout.add_widget(datebutton)

        backlightbutton = BacklightButton(size_hint=(1.0,1.0))
        layout.add_widget(backlightbutton)
        return layout

    def build_right(self):
        # create right column
        layout = BoxLayout(orientation='vertical')

        alarm1 = AlarmButton(text='Alarm 1')
        layout.add_widget(alarm1)

        alarm2 = AlarmWidget(text='Alarm 2')
        layout.add_widget(alarm2)

        return layout

    def build(self):
        # create "root" box layout, where all the action really is...
        root = BoxLayout(orientation='horizontal')

        # build left column
        left = self.build_left()
        root.add_widget(left)

        # build right column
        right = self.build_right()
        root.add_widget(right)

        return root

if __name__ == '__main__':
    AlarmCenterApp().run()
