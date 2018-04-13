"""
Problem:
Given a string, write a function to reverse it. Do this using a loop, if possible.
"""

class Solution():
    def __init__(self):
        super(Solution, self).__init__()

    def reverse_le_string(self, some_string):
        resid=''
        myfavouritelist = [str(some_string[-k-1]) for k in range(len(some_string))]
        for elem in myfavouritelist:
            resid += elem
        return resid

kernel = Solution()
print(kernel.reverse_le_string('hello world'))

