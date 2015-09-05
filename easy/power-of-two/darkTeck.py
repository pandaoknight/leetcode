class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print "================";
        print n
        if n <= 0:
            return False
        while not n & 1023:
            n = n >> 9
        #while not n & 7:
        #    n = n >> 3
        return self._darkTeck(n)

    def _darkTeck(self, n):
        while not n & 1:
            n = n >> 1
        return n == 1

s = Solution()
print s.isPowerOfTwo(0)
print s.isPowerOfTwo(1)
print s.isPowerOfTwo(2)
print s.isPowerOfTwo(3)
print s.isPowerOfTwo(4)
print s.isPowerOfTwo(1024)
print s.isPowerOfTwo(2048)
print s.isPowerOfTwo(3072)
print s.isPowerOfTwo(4333)
print s.isPowerOfTwo(4444)
print s.isPowerOfTwo(4376)
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
