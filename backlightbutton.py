# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

## python imports
from pathlib import Path

import kivy
kivy.require('1.10.0')

## kivy imports
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.logger import Logger

## custom button that turns the backlight on/off
class BacklightButton(Button):
    markup = True
    bl_power = "/sys/class/backlight/rpi_backlight/bl_power"

    def backlight_on(self, instance):
        print("Backlight ON")

        if Path(self.bl_power).exists():
             with open(self.bl_power, "w") as text_file:
                text_file.write("0")

    def backlight_off(self):
        print("Backlight OFF")

        if Path(self.bl_power).exists():
             with open(self.bl_power, "w") as text_file:
                text_file.write("1")

    def launch_popup(self):
        button = Button()

        popup = Popup(title='Backlight', content=button, size_hint=(1.0, 1.0))
        popup.bind(on_dismiss=self.backlight_on)
        button.bind(on_press=popup.dismiss)

        self.backlight_off()
        popup.open()

    def on_press(self):
        self.launch_popup()

    def __init__(self, **kwargs):
        super(BacklightButton,self).__init__(**kwargs)
        self.text = "Backlight [b]Off[/b]"
        self.font_size = self.height/3.0
