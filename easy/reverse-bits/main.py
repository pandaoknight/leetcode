# -*- coding:utf-8 -*-
# description: 32位按位反转
# 因为Python 2.6/2.7 在64位系统下：maxint是2^63，是满足32位unsign的需要的。
# 所以循环32次反转即可。不用考虑在reverse_int的时候的溢出问题。
# 另外16进制也不会有反转问题。倒是8进制可能有。因为8进制一个位是3个bit，所以，32位整型：1000 0000 00 7，反转后7 00 0000 0001是溢出的。
import sys
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in xrange(0, 32):
            bit = n & 1
            #print "%d %d" % (i, bit)
            n = n >> 1
            result = result << 1
            if bit:
                result |= 1
        return result;

if "__main__" == __name__:
    print "-*- test sys.maxint -*-"
    print sys.maxint
    print "-*- test sys.maxint END -*-"
    s = Solution()
    print s.reverseBits(43261596)
    print "964176192 is expected."
