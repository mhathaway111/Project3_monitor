from microbit import *
import math

import radio
chnl = 13 #change channel to your team number

radio.config(channel=chnl)
radio.on()

while True:
    ax_2 = str(accelerometer.get_x())
    radio.send(ax_2)