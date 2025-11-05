class Solution(object):
    def sumOfThree(self, num):
        if not num % 3:
            x = num / 3
            return [x - 1, x ,x + 1]
        return []
        