# RECEIVING MICROBIT

from microbit import *
import math
import radio
import music
from light_and_sound import *


chnl = 13 #change channel to your team number

radio.config(channel=chnl)
radio.on()

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
    sleep(250)

    if ax_t >= 1100:
        Warning()
    else:
        music.stop()
        
        


    

    


