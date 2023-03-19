'''
Rect Area Function
Pawelski
3/19/2023
Python II

Instructions:
In what order are the arguments passed to the parameters?
What would happen if you use the call rectangle_area(4)?
'''

def rectangle_area(length, width):
    '''
    Calculates and displays the area of a rectangle
    with the given length and width.
    '''
    area = length * width
    print("Area:", area)

rectangle_area(4, 7)