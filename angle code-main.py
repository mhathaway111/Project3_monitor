# Imports go at the top
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
    


