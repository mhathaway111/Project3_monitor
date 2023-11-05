# RECEIVING MICROBIT

from microbit import *
import math
import radio
import music
from light_and_sound import *


chnl = 13 #change channel to your team number

radio.config(channel=chnl)
radio.on()

# baby dimensions in inches
n = 3 # neck length
l = 8 # distance from shoulder to top of head

max_angle = math.degrees(math.asin( (l-n) / (l+n) ))

# Code in a 'while True:' loop repeats forever
while True:

    music.stop()

    ax_2 = 0
    received_data = radio.receive()
    
    if received_data is not None:
        try:
            ax_2 = float(received_data)
        except ValueError:
            ax_2 = 0 
     
    ax_1 = accelerometer.get_x()
    ax_t = abs(ax_1 - ax_2)

    read_angle = math.degrees(math.atan(ax_t / 9.8))

    if read_angle >= max_angle:
        Warning()
    else:
        music.stop()
        
        


    

    


