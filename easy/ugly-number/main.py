class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if 0 >= num:
            return False
        while not num % 5:
            num = num / 5
        while not num % 3:
            num = num / 3
        while not num % 2:
            num = num / 2
        return 1 == num

s = Solution()
print s.isUgly(0)
print s.isUgly(1)
print s.isUgly(3)
print s.isUgly(15)
print s.isUgly(14)
print s.isUgly(77)
