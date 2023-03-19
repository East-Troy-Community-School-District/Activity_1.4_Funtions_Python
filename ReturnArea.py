'''
Return Area
Pawelski
3/19/2023
Python II

Instructions:
Why does the program not display anything?

Modify the program so that it prints the returned value
to the shell.

Modify the program so that it calculates the area of 5
rectangles that are 5 by 2. Store the result in a variable
and display the result to the console.
'''

def rectangle_area(length, width):
    '''
    Returns the area of a rectangle with the given
    length and width.
    '''
    area = length * width
    return area

rectangle_area(5, 2)
