class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        ret = [[1]]
        for i in xrange(1, numRows):
            curr = [1]
            for j in xrange(1, i):
                curr.append(ret[i-1][j-1] + ret[i-1][j])
            curr.append(1)
            ret.append(curr)
        return ret

if "__main__" == __name__:
    s = Solution()
    print s.generate(0)
    print s.generate(5)
    print s.generate(15)
