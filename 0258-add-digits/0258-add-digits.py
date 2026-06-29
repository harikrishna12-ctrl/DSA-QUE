class Solution(object):
    def addDigits(self, num):

        if num < 10:
            return num

        total = 0

        while num != 0:
            total = total + (num % 10)
            num = num // 10

        return self.addDigits(total)