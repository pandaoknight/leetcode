#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    【思路】
    没有想出来。看了hints和submission后，发现S(i,j)=S(0,j)-S(0,i) 实在是太经典了。然后，这就是一个two-sum问题了。
    """
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum2count = {0:1}
        total_count = 0
        sum = 0
        for index, num in enumerate(nums):
            sum += num
            total_count += sum2count.get(sum - k, 0)
            sum2count[sum] = sum2count.get(sum, 0) + 1
        return total_count

if "__main__" == __name__:
    s = Solution()
    nums = [24, 2, 10, 8, 6, 4, 14]
    print s.subarraySum(nums, 18)  # 3: 10+8, 4+10, 8+6+4
    print s.subarraySum(nums, 20)  # 1: 2+10+8
    print s.subarraySum(nums, 12)  # 1: 2+10
    print s.subarraySum(nums, 26)  # 2: 24+2, 2+10+8+6

    nums = [1, 1, 1]
    print s.subarraySum(nums, 2)  # 2: 1+1, 1+1