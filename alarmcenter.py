# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

## python imports
# import datetime
# import time
# from time import strftime
# from functools import partial

## kivy imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.togglebutton import ToggleButton
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.config import Config
# from kivy.clock import Clock
# from kivy.properties import StringProperty, NumericProperty, ObjectProperty, BooleanProperty
# from kivy.uix.textinput import TextInput
# from kivy.core.window import Window
# from kivy.uix.vkeyboard import VKeyboard
# from kivy.uix.spinner import Spinner

# launch as fullscreen application
# Config.set('graphics', 'fullscreen', 'auto')
# Config.set('kivy', 'keyboard_mode', 'dock')
# Config.set('kivy', 'keyboard_layout', 'numeric.json')

# main
class AlarmCenterApp(App):
    def build(self):
        return Label(text="Hello from AlarmCenter")

if __name__ == '__main__':
    AlarmCenterApp().run()
