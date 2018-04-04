"""
Problem:
Write a function that takes in a number between 1 and 100 and tries to guess it. 
Based on whether a guess is larger or smaller than the input number, the code 
would come up with a new guess until it gets it right.
"""

class Problem2():
    def __init__(self):
        super(Problem2, self).__init__()

    def guesser(self, number):
        low = 0
        high = 100
        pivot = (high - low) // 2

        for k in range(8):
            if number == pivot :
                print('Oh I know! Your number is {}! Took me {} tries.'.format(pivot, k))
                return None

            elif number > pivot:
                low = pivot
            elif number < pivot:
                high = pivot

            pivot = low + (high-low) // 2

kernel = Problem2()
kernel.guesser(17)
