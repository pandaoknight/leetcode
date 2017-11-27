#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    """
    【思路】
    1. 这里我们使用hashtable，而python中的dict就是hashtable
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        traveled = {}
        for index, n in enumerate(nums):
            index = index+1
            target_index = traveled.get(target-n)
            if None != target_index:
                return [target_index, index]
            else:
                traveled[n] = index
        return None

if "__main__" == __name__:
    s = Solution()
    print s.twoSum([1, 2, 3, 4, 5,], 9)
    print s.twoSum([2, 7, 11, 15], 9)


