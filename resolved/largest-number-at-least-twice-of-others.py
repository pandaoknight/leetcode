class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MULTI = 2
        inferior, dominant, dominant_index = -1, float("-inf"), -1
        for k, num in enumerate(nums):
            if num > dominant:
                inferior = dominant
                dominant = num
                dominant_index = k
        if dominant >= inferior * MULTI:
            return dominant_index
        else:
            return -1


if "__main__" == __name__:
    s = Solution()
    print s.dominantIndex([3, 6, 1, 0])
    print s.dominantIndex([1, 2, 3, 4])
    print s.dominantIndex([1, 2, 3, 4, 8])
    print float("-inf")
