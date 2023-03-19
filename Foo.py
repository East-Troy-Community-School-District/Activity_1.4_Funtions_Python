'''
Return Area
Pawelski
3/19/2023
Python II

Instructions:
Why is x in the function different than x in the main?

Uncomment the last line and run the program. Why does the
line produce an error?

How can we make y a global variable?

Try modifying the variable global_var in the function.
Can you change the global copy? Modify the function so
it changes the global copy.
'''

def foo(x):
    '''
    Demonstrates scope.
    '''
    y = 4
    print("Function x:", x)
    print("Function y:", y)
    print("Function global_var:", global_var)

global_var = "Anywhere..."
x = 5
foo(3)
print("Main x:", x)
print("Main global_var:", global_var)
# print("Main y:", y)
