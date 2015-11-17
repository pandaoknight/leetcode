class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = range(2, n)
        p = []
        #product = 1
        while s:
            current = s.pop(0)
            p.append(current)
            #product *= current
            #debug
            #print p
            #filter = []
            for i in s:
                #if i > current + product:
                #    break
                #if 0 == i % current:
                #    filter.append(i)
                if 0 == i % current:
                    s.remove(i)
        return len(p)

if "__main__" == __name__:
    s = Solution()
    print s.countPrimes(100)
    print s.countPrimes(2)
    print s.countPrimes(0)
    print s.countPrimes(4999)
    print s.countPrimes(49990)
    print s.countPrimes(499900)
    print s.countPrimes(1499900)
