# Alarm Center for Raspberry Pi
#
# Copyright 2017 Shaun Thompson <shaun.b.thompson@gmail.com>
#

import urllib3
import json

import kivy
kivy.require('1.10.0')

## kivy imports
from kivy.uix.button import Button
from kivy.clock import Clock

## custom button that displays weather for selected loation
class WeatherButton(Button):
    markup = True

    def _update(self, dt):
        self.text = 'asdf'

        http = urllib3.PoolManager()
        response = http.request('GET', 'http://api.wunderground.com/api/cdb8e4841f7edece/geolookup/conditions/q/FL/Orlando.json')
        json_string = response.data.decode('utf8')
        parsed_json = json.loads(json_string)
        location = parsed_json['location']['city']
        temp_f = parsed_json['current_observation']['temperature_string']
        self.text = ("[b]%s[/b] %s" % (location, temp_f))
        response.close()

    def __init__(self, **kwargs):
        super(WeatherButton,self).__init__(**kwargs)
        self.font_size = self.height/3.0
        Clock.schedule_interval(self._update, 10.0)
        self._update(0)
