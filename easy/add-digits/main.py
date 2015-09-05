class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if 0 == num:
            return 0
        n = num % 9
        return 9 if not n else n
