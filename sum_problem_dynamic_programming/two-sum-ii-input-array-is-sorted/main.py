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

        count = -1
        while nums:
            a = nums.pop(0)
            count += 1
            index, lnums, rnums = self.sortedListBinarySplit(nums, target - a)
            if None != index:
                return [count, count + index + 1]
            nums = lnums

        return None

    def sortedListBinarySplit(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype index: None or int
        :rtype lnums: list[int]
        :rtype rnums: list[int]
        """
        if nums[0] >= target:
            if nums[0] == target:
                return 0, [], nums[1:]
            else:
                return None, [], nums
        if nums[-1] <= target:
            if nums[-1] == target:
                return len(nums)-1, nums[:-1], []
            else:
                return None, nums, []

        l, r = 0, len(nums)-1
        while l+1 != r:
            m = (l+r)/2
            if nums[m] == target:
                return m, nums[:m], nums[m+1:]
            if nums[m] > target:
                r = m
            else:
                l = m
        index, lnums, rnums = None, nums[:r], nums[r:]
        return index, lnums, rnums


if "__main__" == __name__:
    test_s = Solution()
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 0)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 16)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 2)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 15)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 7)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 8)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 11)
    print "==========================="
    print test_s.sortedListBinarySplit([2,], 2)
    print test_s.sortedListBinarySplit([2, 2, 2, 2, 2], 2)
    print test_s.sortedListBinarySplit([2, 2,], 2)
    print test_s.sortedListBinarySplit([2, 2, 2, 2, 2], 2)

    s = Solution()
    print s.twoSum([2, 7], 9)
    print s.twoSum([2, 7 ,11, 15], 9)
    print s.twoSum([2, 7 ,11, 15], 22)
    print s.twoSum([2, 3, 7 ,11, 15], 14)
    print s.twoSum([2, 3, 7 ,11, 15], 15)

    print s.twoSum([3, 3], 6)
    print s.twoSum([2, 3, 7, 7, 11, 15], 14)
    print s.twoSum([2, 3, 4, 7, 7, 11, 15], 14)
