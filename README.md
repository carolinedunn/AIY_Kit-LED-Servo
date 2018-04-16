# AIY_Kit-LED-Servo
Using the AIY Voice Kit with LEDs and Servo Motors

There are 3 projects in this repository.
1) Turn on and off [4 LEDs](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/4leds.py)
2) Control [2 Servo motors](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/servo.py)
3) Control [2 Servo Motors and 4 LEDs](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/servo-led.py)

### Pre-Requisite: Please enable billing by completing the Cloud Speech API tutorial first. https://aiyprojects.withgoogle.com/voice-v1/#makers-guide-change-to-the-cloud-speech-api

# Project 1 - Turn on and off 4 LEDs
1. Connect LEDs per this wiring diagram.


2. Use your favorite text editor to create your new file:
```
nano src/led.py
```

3. Copy the code from [4leds.py](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/4leds.py) and paste into your led.py file.

4. Save and close led.py by:
```
Ctrl-X
y
[Enter]
```
5. Make the file you just created executable.
```
chmod +x /src/led.py
```

6. Run the file you just created.
```
src/led.py
```

You should be able to command your AIY Kit with the following commands:
> Ok Google, Red light on.

> Ok Google, Red light off.

> Ok Google, Blue light on.

> Ok Google, Blue light off.

> Ok Google, Green light on.

> Ok Google, Green light off.

> Ok Google, Yellow light on.

> Ok Google, Yellow light off.

> Ok Google, Primary colors on.

> Ok Google, Primary colors off.

> Ok Google, All lights on.

> Ok Google, All lighs off.

# Project 2 - Control 2 Servo Motors
1. Connect 2 servo motors per this wiring diagram. I purchased [servo motors here](https://amzn.to/2HrBd5G)


2. Use your favorite text editor to create your new file:
```
nano src/servo.py
```

3. Copy the code from [servo.py](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/servo.py) and paste into your servo.py file.

4. Save and close servo.py by:
```
Ctrl-X
y
[Enter]
```
5. Make the file you just created executable.
```
chmod +x /src/servo.py
```

6. Run the file you just created.
```
src/servo.py
```

You should be able to command your AIY Kit with the following commands:
> Ok Google, wave.
