"""
Problem:
Write a function that takes in a number between 1 and 100 and tries to guess it. 
Based on whether a guess is larger or smaller than the input number, the code 
would come up with a new guess until it gets it right.
"""

class Problem2():
    def __init__(self, number):
        super(Problem2, self).__init__()

        self.low = 0
        self.high = 100
        self.number = number
        self.pivot = (self.high - self.low) // 2
        print('initialization: guessing number: {} with initial pivot: {}'.format(self.number, self.pivot))

    def logic(self):
        for k in range(8):
            print('iter {}: low: {}, high: {}, pivot: {}, number: {}'.format(k, self.low, self.high, self.pivot,
            self.number))

            if self.number == self.pivot :
                print('oh I know! your answer is {}!'.format(self.pivot))
                return self.pivot

            elif self.number > self.pivot:
                self.low = self.pivot

            elif self.number < self.pivot:
                self.high = self.pivot

            self.pivot = self.low + (self.high-self.low) // 2

problem2 = Problem2(42)

problem2.logic()


