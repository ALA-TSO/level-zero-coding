task 0.5

import math

def area_of_triangle(x,y,z):
    s = 1/2 * (x + y + z) 
    a = math.sqrt(s*(s - x)*(s - y)*(s - z))
    print(a)

area_of_triangle(3, 4, 5)
