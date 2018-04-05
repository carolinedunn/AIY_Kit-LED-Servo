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

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
from time import sleep
from gpiozero import Servo

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('maximum')
    recognizer.expect_phrase('minimum')
    recognizer.expect_phrase('middle')
    recognizer.expect_phrase('wave')
    
    button = aiy.voicehat.get_button()
    aiy.audio.get_recorder().start()

    servo1 = Servo(26)
    servo2 = Servo(6)

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        if text is None:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'maximum' in text:
                print('Moving servo to maximum')
                servo1.max()
                servo2.max()
            elif 'minimum' in text:
                print('Moving servo to minimum')
                servo1.min()
                servo2.min()
            elif 'middle' in text:
                print('Moving servo to middle')
                servo1.mid()
                servo2.mid()
            elif 'wave' in text:
                print('I am waving at you.')
                servo1.max()
                servo2.max()
                sleep(1)
                servo1.min()
                servo2.min()
                sleep(1)
                servo1.max()
                servo2.max()
                sleep(1)
                servo1.min()
                servo2.min()

if __name__ == '__main__':
    main()