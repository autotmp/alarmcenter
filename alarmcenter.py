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

    def build_left(self):
        # create left column
        layout = BoxLayout(orientation='vertical')

        timebutton = TimeButton(text='Time', size_hint=(1.0, 1.0))
        layout.add_widget(timebutton)

        datebutton = DateButton(text='Date', size_hint=(1.0, 0.4))
        layout.add_widget(datebutton)

        backlightbutton = BacklightButton(size_hint=(1.0,0.4))
        layout.add_widget(backlightbutton)
        return layout

    def build_right(self):
        # create right column
        layout = BoxLayout(orientation='vertical')

        alarm1 = AlarmWidget(name='Alarm 1')
        layout.add_widget(alarm1)
        #layout.add_widget(Label(text='[b]Alarm 1[/b]', size_hint=(1.0,0.1), markup='True'))

        alarm2 = AlarmWidget(name='Alarm 2')
        layout.add_widget(alarm2)
        #layout.add_widget(Label(text='[b]Alarm 2[/b]', size_hint=(1.0,0.1), markup='True'))

        weather = WeatherButton(text='Weather')
        layout.add_widget(weather)
        return layout

    # def on_stop(self):
    #     # The Kivy event loop is about to stop, set a stop signal;
    #     # otherwise the app window will close, but the Python process will
    #     # keep running until all secondary threads exit.
    #     print("stop operations")

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
    # Window.fullscreen = True
    AlarmCenterApp().run()
