import gpiozero as gpio
import time

# setup row and column pins on rpi
ROW = [27, 5, 13, 19]
COL = [12, 16, 20]

KEYS = [    ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "#"]]

# set columns as output pins and set them to 1
OUT = []
for ci in COL:
    d = gpio.OutputDevice(ci, True, True)
    OUT.append(d)

# set rows as input pins with pull_up resistor
IN = []
for ri in ROW:
    d = gpio.InputDevice(ri, True)
    IN.append(d)

"""
pressed button when high from pull_up resistor, meets with low from looping through outputs.
"""
while True:
    for outI in range(len(OUT)):
        OUT[outI].off()
        for inI in range(len(IN)):
            # input is active when output=0 and input(pull_up)=1
            if IN[inI].is_active == True:
                print("pressed", KEYS[inI][outI])
                # do nothing while button is pressed
                while IN[inI].is_active == True:
                    pass
        OUT[outI].on()
    # some timeout to avoid multipresses
    time.sleep(0.1)
