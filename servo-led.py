#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import platform
import subprocess
import sys

import aiy.assistant.auth_helpers
from aiy.assistant.library import Assistant
import aiy.audio
import aiy.voicehat
from time import sleep
from gpiozero import Servo
from google.assistant.library.event import EventType

import RPi.GPIO as GPIO
servo1 = Servo(26)
servo2 = Servo(6)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def red_led_on():
    aiy.audio.say('Red light on')
    GPIO.output(13,GPIO.HIGH)

def red_led_off():
    aiy.audio.say('Red light off')
    GPIO.output(13,GPIO.LOW)

def blue_led_on():
    aiy.audio.say('Blue light on')
    GPIO.output(5,True)

def blue_led_off():
    aiy.audio.say('Blue light off')
    GPIO.output(5,False)

def green_led_on():
    aiy.audio.say('Green light on')
    GPIO.output(12,True)

def green_led_off():
    aiy.audio.say('Green light off')
    GPIO.output(12,False)
    
def yellow_led_on():
    aiy.audio.say('Yellow light on')
    GPIO.output(24,True)

def yellow_led_off():
    aiy.audio.say('Yellow light off')
    GPIO.output(24,False)
    
def all_led_on():
    aiy.audio.say('Turning all lights on')
    GPIO.output(13,True)
    GPIO.output(5,True)
    GPIO.output(12,True)
    GPIO.output(24,True)

def all_led_off():
    aiy.audio.say('Turning all lights off')
    GPIO.output(13,False)
    GPIO.output(5,False)
    GPIO.output(12,False)
    GPIO.output(24,False)

def primary_on():
    aiy.audio.say('Turning on blue, red, and yellow lights.')
    GPIO.output(13,True)
    GPIO.output(5,True)
    GPIO.output(12,False)
    GPIO.output(24,True)

def primary_off():
    aiy.audio.say('Turning off primary colors.')
    GPIO.output(13,False)
    GPIO.output(5,False)
    GPIO.output(24,False)

def wave():
    aiy.audio.say('Hi. I am waving at you.')
    GPIO.output(13,True)
    GPIO.output(5,True)
    GPIO.output(12,True)
    GPIO.output(24,True)
    servo2.max()
    sleep(1)
    servo2.min()
    sleep(1)
    servo1.max()
    sleep(1)
    servo1.min()
    sleep(1)
    GPIO.output(13,False)
    GPIO.output(5,False)
    GPIO.output(12,False)
    GPIO.output(24,False)

def power_off_pi():
    aiy.audio.say('Shutting down.')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.audio.say('Rebooting now.')
    subprocess.call('sudo reboot', shell=True)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))


def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == 'reboot':
            assistant.stop_conversation()
            reboot_pi()
        elif text == 'ip address':
            assistant.stop_conversation()
            say_ip()
        elif text == 'red light on':
            assistant.stop_conversation()
            red_led_on()
        elif text == 'red light off':
            assistant.stop_conversation()
            red_led_off()
        elif text == 'blue light on':
            assistant.stop_conversation()
            blue_led_on()
        elif text == 'blue light off':
            assistant.stop_conversation()
            blue_led_off()
        elif text == 'green light on':
            assistant.stop_conversation()
            green_led_on()
        elif text == 'green light off':
            assistant.stop_conversation()
            green_led_off()
        elif text == 'yellow light on':
            assistant.stop_conversation()
            yellow_led_on()
        elif text == 'yellow light off':
            assistant.stop_conversation()
            yellow_led_off()
        elif text == 'primary colors on':
            assistant.stop_conversation()
            primary_on()
        elif text == 'primary colors off':
            assistant.stop_conversation()
            primary_off()
        elif text == 'traffic caution':
            assistant.stop_conversation()
            traffic_caution()
        elif text == 'all lights on':
            assistant.stop_conversation()
            all_led_on()
        elif text == 'all lights off':
            assistant.stop_conversation()
            all_led_off()
        elif text == 'wave':
            assistant.stop_conversation()
            wave()
 
    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    if platform.machine() == 'armv6l':
        print('Cannot run hotword demo on Pi Zero!')
        exit(-1)

    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()