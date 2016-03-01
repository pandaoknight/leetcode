class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        acc = accumulator = 0
        for c in s:
            acc *=26
            acc += ord(c) - ord("A") + 1
        return acc

if "__main__" == __name__:
    s = Solution()
    print s.titleToNumber("A") # 1
    print s.titleToNumber("Z") # 26
    print s.titleToNumber("AA") # 27
    print s.titleToNumber("AZ") # 52
    print s.titleToNumber("ZZ") # 26*26 + 26
    print s.titleToNumber("ZZZ") # 26*26*26 + 26*26 + 26
