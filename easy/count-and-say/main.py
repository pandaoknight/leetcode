class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if 1 == n:
            return "1"

        origin = self.countAndSay(n - 1)
        current = origin[0]
        count = 1
        target = ""
        for val in origin[1:]:
            if current == val:
                count += 1
            else:
                target += str(count) + current
                current = val
                count = 1
        target += str(count) + current
        print target
        return target

if "__main__" == __name__:
    s = Solution()
    print s.countAndSay(30)
    print "1, 11, 21, 1211, 111221, 31221, 13112211, 1113212221, 311312113211 is expected"
