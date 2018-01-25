#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum_0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        head, tail = 0, len(nums)
        while head < tail:
            search_target = target - nums[head]
            search_index = self.searchInsert(nums[head + 1:tail], search_target)
            if head + 1 + search_index < len(nums) and search_target == nums[head + 1 + search_index]:
                return [head, search_index + head + 1]
            tail = search_index + head + 1
            head += 1
        return []


    def searchInsert(self, nums, target):
        start, tail = 0, len(nums)
        while start != tail:
            half = (start + tail)/2
            if target > nums[half]:
                start = half + 1
            else:
                tail = half
        return start

    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for (cur, num) in enumerate(nums):
            index = hash_table.get(target - num, None)
            if index is not None:
                return [index, cur]
            hash_table[num] = cur
        return []

    def twoSum(self, nums, target):
        traveled = {}
        for index, n in enumerate(nums):
            target_index = traveled.get(target - n)
            if None != target_index:
                return [target_index, index]
            else:
                traveled[n] = index
        return None

if "__main__" == __name__:
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 4)  # []
    print s.twoSum([2, 7, 11, 15], 9)  # [0, 1]
    print s.twoSum([2, 7, 11, 15], 13)  # [0, 2]
    print s.twoSum([2, 7, 11, 15], 17)  # [0, 3]
    print s.twoSum([2, 7, 11, 15], 18)  # [1, 2]
    print s.twoSum([2, 7, 11, 15], 22)  # [1, 3]
    print s.twoSum([2, 7, 11, 15], 26)  # [2, 3]
    print s.twoSum([2, 7, 11, 15], 27)  # []

    print s.twoSum([2, 7, 11, 15, 23, 47], 18)  # [1, 2]

