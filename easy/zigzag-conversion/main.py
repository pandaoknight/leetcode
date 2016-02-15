# -*- coding:utf-8 -*-
# description: 核心思想：周期，注意处理尾部的元素
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if 1 == numRows:
            return s
        size = len(s)
        cycle = 2 * numRows - 2
        seq = self.sequence(numRows)
        #return seq
        ret = []
        curr = 0
        while curr < size:
            ret.append(s[curr])
            curr += cycle
        for curr_left, curr_right in seq:
            base = 0
            while base + curr_left < size:
                ret.append(s[base + curr_left])
                if base + curr_right >= size:
                    break
                ret.append(s[base + curr_right])
                base += cycle
        curr = numRows - 1
        while curr < size:
            ret.append(s[curr])
            curr += cycle
        return ''.join(ret)

    def sequence(self, numRows):
        #seq = [0]
        seq = []
        for i in range(1, numRows - 1):
            seq.append( (i, 2 * numRows - 2 - i) )
        #seq.append(numRows - 1)
        return seq

# input:
# PAYPALISHIRING
#
# medium(middle word):
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# output:
# PAHNAPLSIIGYIR
#
# @Me: The sample of question is abitrary. That a bad idea.
#

if "__main__" == __name__:
    s = Solution()
    print s.convert("PAYPALISHIRING", 1)
    print s.convert("PAYPALISHIRING", 2)
    print s.convert("PAYPALISHIRING", 3)
    print s.convert("abcdefghijklmnopqrstuvwxyz", 4) # first circle: abcdef
    print s.convert("abcdefghijklmnopqrstuvwxyz", 5) # abcdefgh
    print s.convert("abcdefghijklmnopqrstuvwxyz", 6) # abcdefghij

    print s.convert("abcdef", 3)

#TODO: Inverse solution.
