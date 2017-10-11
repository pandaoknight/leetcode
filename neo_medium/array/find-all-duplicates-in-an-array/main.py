#!/usr/bin/python
# -*- coding:utf-8 -*-
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        d = [0] * l
        for n in nums:
            if n > l:
                return None
            d[n - 1] += 1
        return filter(lambda x: d[x-1] > 1, xrange(1, l+1))

if "__main__" == __name__:
    s = Solution()
    print s.findDuplicates([1, 2, 3, 4, 5, 6, 7, 8])
    print s.findDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 8])
    print s.findDuplicates([1, 2, 3, 4, 5, 5, 7, 8])
    print s.findDuplicates([5, 4, 3, 2, 1])
    print s.findDuplicates([1, 5, 4, 3, 2, 1])
    print s.findDuplicates([5, 4, 3, 2, 1])
    print s.findDuplicates([5, 4, 3, 2, 1, 1])
    print s.findDuplicates([5, 4, 3, 2, 1, 5, 4, 3, 2, 1])
    print s.findDuplicates([5, 5, 4, 4, 3, 3, 2, 2, 1, 1])
