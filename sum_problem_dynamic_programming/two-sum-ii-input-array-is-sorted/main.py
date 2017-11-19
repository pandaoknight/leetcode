#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: Listint]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return None
        while nums:
            

        return None



if "__main__" == __name__:
    s = Solution()
    print s.twoSum([2, 7], 9)
    print s.twoSum([2, 7 ,11, 15], 9)
    print s.twoSum([2, 7 ,11, 15], 22)
    print s.twoSum([2, 3, 7 ,11, 15], 14)
    print s.twoSum([2, 3, 7 ,11, 15], 15)

    print s.twoSum([3, 3], 6)
    print s.twoSum([2, 3, 7, 7, 11, 15], 14)
    print s.twoSum([2, 3, 4, 7, 7, 11, 15], 14)
