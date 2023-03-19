'''
Greeting Function
Pawelski
3/19/2023
Python II

Instructions:
How does the parameter name allow the greeting() function
to be more flexible?
'''

def greeting(name):
    '''
    Displays a simple greeting.
    '''
    print("Hello " + name + "!")

greeting("Frank")
greeting("Jimbo")
user_name = input("Enter you name >> ")
greeting(user_name)
