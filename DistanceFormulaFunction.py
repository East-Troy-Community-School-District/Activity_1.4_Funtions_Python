'''
Distance Formula Function
Pawelski
3/13/2023
Python II
'''

import math

def distance(x1, y1, x2, y2):
    '''Calculates the distance between two points, represented as tuples.'''
    delta_x = x2 - x1
    delta_y = y2 - y1
    distance = math.sqrt(delta_x**2 + delta_y**2)
    return distance

x1 = int(input("Enter the x-value of the first point >> "))
y1 = int(input("Enter the y-value of the first point >> "))
x2 = int(input("Enter the x-value of the second point >> "))
y2 = int(input("Enter the y-value of the second point >> "))
print("Distance:", distance(x1, y1, x2, y2))
