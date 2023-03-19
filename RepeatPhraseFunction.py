'''
Repeat Phrase Function
Pawelski
3/19/2023
Python II

Instructions:
Why do both calls work? What number is used for times
with the call repeat_phrase("hello")? What about
repeat_phrase("goodbye", 3)?

Add a call to the program so that it displays your name
100 times.
'''

def repeat_phrase(phrase, times = 5):
    '''
    Repeats a given phrase a given amount of times.
    If no amount is given, the default is 5.
    '''
    for i in range(0, times):
        print(phrase)

repeat_phrase("hello")
repeat_phrase("goodbye", 3)

