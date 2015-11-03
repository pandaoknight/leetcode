class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        cycle = 2 * numRows - 2
        return s

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
    print s.convert("PAYPALISHIRING", 3)

#TODO: Inverse solution.
