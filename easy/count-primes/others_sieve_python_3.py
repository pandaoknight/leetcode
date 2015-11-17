class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        _xrange = xrange
        nums = range(1, n, 2)
        nums[0] = 0
        count = 1
        n //= 2
        for p in itertools.ifilter(None, nums):
            count += 1
            for q in _xrange(p * p // 2, n, p):
                nums[q] = 0
        return count

if "__main__" == __name__:
    s = Solution()
    print s.countPrimes(100)
    #exit()
    print s.countPrimes(0)
    print s.countPrimes(1)
    print s.countPrimes(2) # null
    print s.countPrimes(3) # 2
    print s.countPrimes(4) # 2 3
    print s.countPrimes(5) # 2 3
    print s.countPrimes(6) # 2 3 5
    print s.countPrimes(7) # 2 3 5
    print s.countPrimes(8) # 2 3 5 8
    print s.countPrimes(4999)
    print s.countPrimes(49990)
    print s.countPrimes(499900)
    print s.countPrimes(1499900)
