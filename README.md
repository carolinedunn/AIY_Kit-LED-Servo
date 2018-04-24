# AIY_Kit-LED-Servo
Using the AIY Voice Kit with LEDs and Servo Motors

There are 3 projects in this repository.
1) Turn on and off [4 LEDs](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/4leds.py)
2) Control [2 Servo motors](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/servo.py)
3) Control [2 Servo Motors and 4 LEDs](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/servo-led.py)

### Pre-Requisite #1 Please enable billing by completing the Cloud Speech API tutorial first. https://aiyprojects.withgoogle.com/voice-v1/#makers-guide-change-to-the-cloud-speech-api

#### Pre-Requisite #2 Create a directory called 'src'
```
mkdir src
```

# Project 1 - Turn on and off 4 LEDs

[YouTube Tutorial Video Here](https://youtu.be/UUunyu2Ua14)

Materials: You will need 4 LEDs (red, blue, green, and yellow), 4 resistors of 330 ohms, wires, and a breadboard (or soldering iron).

1. Connect the Red LED to GPIO26, Blue LED to GPIO6, Green LED to GPIO13, and Yellow LED to GPIO5. Wiring Diagram below.

![alt text](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/LED%20Wiring%20Diagram.jpg)

2. Use your favorite text editor to create your new file:
```
nano src/4led.py
```

3. Copy the code from [4leds.py](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/4leds.py) and paste into your 4led.py file.

4. Save and close 4led.py by:
```
Ctrl-X
y
[Enter]
```
5. Make the file you just created executable.
```
chmod +x /src/4led.py
```

6. Run the file you just created.
```
src/4led.py
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
1. Connect one servo motor to GPIO26, and the second servo motor to GPIO6. You may need to solder header pins to the AIY Voice Hat. Wiring Diagram shown below.

![alt text](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/Servo%20Wiring%20Diagram.jpg)

I purchased [servo motors here](https://amzn.to/2HrBd5G).


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

# Project 3 - Control 2 Servo Motors and 4 LEDs

Materials: You will need 4 LEDs (red, blue, green, and yellow), 4 resistors of 330 ohms, wires, soldering iron, and 2 servo motors. You may need to solder header pins to the AIY Voice Hat.

I purchased [servo motors here](https://amzn.to/2HrBd5G).

1. Connect one servo motor to GPIO26 (left), and the second servo motor to GPIO6 (right). Connect the Red LED to GPIO13, Blue LED to GPIO65, Green LED to GPIO12, and Yellow LED to GPI24.  Wiring Diagram shown below.
![alt text](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/LED-Servo%20Wiring%20Diagram.jpg)

2. Use your favorite text editor to create your new file:
```
nano src/ledservo.py
```

3. Copy the code from [servo-led.py](https://github.com/carolinedunn/AIY_Kit-LED-Servo/blob/master/servo-led.py) and paste into your ledservo.py file.

4. Save and close ledservo.py by:
```
Ctrl-X
y
[Enter]
```
5. Make the file you just created executable.
```
chmod +x /src/ledservo.py
```

6. Run the file you just created.
```
src/ledservo.py
```

You should be able to command your AIY Kit with the following commands:

> Ok Google, wave.

> Ok Google, wave right arm.

> Ok Google, wave left arm.

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
