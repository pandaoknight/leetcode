class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #print "-----------"
        #print n
        if n <= 0:
            return False
        #print n & 1
        while not n & 1:
            n = n >> 1
            #print "debug:"+str(n)
        return n == 1


s = Solution()
print s.isPowerOfTwo(0)
print s.isPowerOfTwo(1)
print s.isPowerOfTwo(2)
print s.isPowerOfTwo(3)
print s.isPowerOfTwo(4)
print s.isPowerOfTwo(768)

print '================='
a = 5
print a & 1
a = a >> 1
print a
print '================='

print a & 1
a = a >> 1
print a
print '================='

print a & 1
a = a >> 1
print a
