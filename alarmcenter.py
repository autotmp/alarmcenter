# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

import kivy
import threading
kivy.require('1.10.0')

## kivy imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.logger import Logger

## custom imports
from timebutton import TimeButton
from datebutton import DateButton
from backlightbutton import BacklightButton
from alarmwidget import AlarmWidget
from weatherbutton import WeatherButton

# launch as fullscreen application
Config.set('graphics', 'fullscreen', 'auto')
Config.set('kivy', 'log_dir', 'logs')
Config.set('kivy', 'log_enable', '1')
Config.set('kivy', 'log_level', 'info')
Config.set('kivy', 'log_name', 'alarmcenter_%y-%m-%d-%_.txt')
#Config.read('kivyconfig.ini')
#Config.write()

# main
class AlarmCenterApp(App):

    # def on_stop(self):
    #     # The Kivy event loop is about to stop, set a stop signal;
    #     # otherwise the app window will close, but the Python process will
    #     # keep running until all secondary threads exit.
    #     print("stop operations")

    def build_alarm_stack(self):
        layout = BoxLayout(orientation='vertical')

        alarm1 = AlarmWidget(name='Alarm 1', size_hint=(1.0, 1.0))
        layout.add_widget(alarm1)

        alarm2 = AlarmWidget(name='Alarm 2', size_hint=(1.0, 1.0))
        layout.add_widget(alarm2)
        return layout

    def build_date_stack(self):
        layout = BoxLayout(orientation='vertical')

        datebutton = DateButton(text='Date', size_hint=(1.0, 1.0))
        layout.add_widget(datebutton)

        weather = WeatherButton(text='Weather', size_hint=(1.0, 1.0))
        layout.add_widget(weather)
        return layout

    def build(self):
        # create "root" layout
        root = BoxLayout(orientation='vertical')

        # create "TIME" button
        timebutton = TimeButton(text='Time', size_hint=(1.0, 1.0))
        root.add_widget(timebutton)

        # create "MIDDLE" layout
        middle = BoxLayout(orientation='horizontal')
        datestack = self.build_date_stack()
        middle.add_widget(datestack)
        alarmstack = self.build_alarm_stack()
        middle.add_widget(alarmstack)
        root.add_widget(middle)

        # create "BACKLIGHT" button
        backlight = BacklightButton(size_hint=(1.0,0.3))
        root.add_widget(backlight)

        return root

if __name__ == '__main__':
    # Window.fullscreen = True
    AlarmCenterApp().run()
