# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:43:33 2023

@author: mkhda
"""
#10/12/23#################################################################

# Determines angle between the two microbits
from microbit import *
import math as m

def calc_angle(a,b): # a and b are each lists with three items (positions from each microbit)
    #dot product of a and b
    mult_values = []
    n = 0
    for item in a:
        x = item*b[n]
        mult_values.append(x)
        n += 1
    a_dot_total = mult_values[0]+mult_values[1]+mult_values[2]
    #magnitude 
    mag_a = m.sqrt((a[0]**2)+(a[1]**2)+(a[2]**2))
    mag_b = m.sqrt((b[0]**2)+(b[1]**2)+(b[2]**2))    
    #finding theta
    value = a_dot_total / (mag_a*mag_b)
    angle = m.acos(value)
    return(angle)
    

# Determines position -- needs to be used for each microbit
from microbit import *

def def_position(x,y,z):
    times = running_time.ticks_ms()
    delta_times = running_time.ticks_diff(times)
    acceleration = [x,y,z]
    position = []
    for item in acceleration:
        i = (item/2)*(delta_times[0]**2) 
        position.append(i)
    return(position) # a three item list of x y and z coordinates
        
def main():
    while True:
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        z = accelerometer.get_z()

        p = def_position(x,y,z)
   

main()



#####################################################################

import scipy as s


def def_position(x,y,z):
   acceleration = [x,y,z]
   position = []
   for i in acceleration:
       a = s.integrate.dblquad(i)
       position.append(a)
   
def def_position(x,y,z):
    t = 1 #number to be determined by time between data point collection
    acceleration = [x,y,z]
    position = []
    for item in acceleration:
        i = (item/2)*(t**2) 
        
def main():
    while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    def_position(x,y,z)