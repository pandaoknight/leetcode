class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        begin = nums[0]
        last = begin
        result = []
        for n in nums[1:]:
            if last + 1 == n:
                last = n
            else:
                result.append((begin, last))
                last = n
                begin = n
        result.append((begin, last))
        map_reduce = []
        for a,b in result:
            if a == b:
                map_reduce.append(str(a))
            else:
                map_reduce.append("%d->%d" % (a,b))
        return map_reduce

if "__main__" == __name__:
    s = Solution()
    print s.summaryRanges([0,1,2,4,5,7])
    print s.summaryRanges([])
