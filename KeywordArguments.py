'''
Keyword Arguments
Pawelski
3/19/2023
Python II

Instructions:
How are keyword arguments useful? Have you seen them
before?
'''
  
def repeat_phrase(phrase, times):
    '''
    Repeats a given phrase a given amount of times.
    '''
    for i in range(0, times):
        print(phrase)

repeat_phrase(phrase = "Guten Tag", times = 4)
repeat_phrase(times = 4, phrase = "Guten Nacht")