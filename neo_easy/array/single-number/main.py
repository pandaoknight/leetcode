#!/usr/bin/python
# -*- coding:utf-8 -*-
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for n in nums:
            if dict.get(n):
                del dict[n]
            else:
                dict[n] = True
        return dict.keys()[0]
        

if "__main__" == __name__:
    s = Solution()
    print s.singleNumber([1, 2, 3, 2, 3])
    print s.singleNumber([1, 2, 3, 2, 3, 1, 4, 5, 5])
