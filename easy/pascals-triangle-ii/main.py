# -*- coding: utf-8 -*-
# description: Pascal’s triangle
# 不同的民族的人都有图文记载研究这个数学模型，我大天朝喜欢将其称之为杨辉三角。
# 而400年后的法国物理学家、数学家Pascal帕斯卡，真正的功绩在于整理出了其二项式表达式。
#
# 所以，此题可以不用一级级推导，而是直接使用数学表达式进行计算。
#
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

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.generate(rowIndex+1)[rowIndex]

if "__main__" == __name__:
    s = Solution()
    print s.getRow(0)
    print s.getRow(1)
    print s.getRow(2)
    print s.getRow(3)
