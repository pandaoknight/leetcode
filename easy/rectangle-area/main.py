class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        ac = (A, C)
        eg = (E, G)
        #print self.segLen(ac)
        #print self.segsOverlapping(ac, eg)
        bd = (B, D)
        fh = (F, H)
        #return self.segLen(ac) * self.segLen(bd)
        #return self.segLen(eg) * self.segLen(fh)
        #return self.segsOverlapping(ac, eg) * self.segsOverlapping(bd, fh)
        return self.segLen(ac) * self.segLen(bd) + self.segLen(eg) * self.segLen(fh) - self.segsOverlapping(ac, eg) * self.segsOverlapping(bd, fh)

    def segLen(self, seg):
        return max(seg) - min(seg)

    def segsOverlapping(self, seg, another):
        segStart = min(seg)
        segEnd = max(seg)
        anotherStart = min(another)
        anotherEnd = max(another)
        # let anotherEnd be the bigger one
        if anotherEnd < segEnd:
            segStart, anotherStart = anotherStart, segStart
            segEnd, anotherEnd = anotherEnd, segEnd
        return max(0, segEnd - max(segStart, anotherStart))

if "__main__" == __name__:
    s = Solution()
    print s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
