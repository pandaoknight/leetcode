class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 2 >= n:
            return 0
        if 3 == n:
            return 1
        if 5 >= n:
            return 2
        if 6 >= n:
            return 3
        p = [3, 5]
        index = 1
        max = p[index] ** 2
        tester = p[:index]
        for current in xrange(7, n, 2):
            if max == current:
                index += 1
                max = p[index] ** 2
                tester = p[:index]
            isPrime = 1
            for t in tester:
                if 0 == current % t:
                    isPrime = 0
                    break
            if isPrime:
                p.append(current)
            #print "%d %s" % (current, p)
        return len(p) + 1

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
