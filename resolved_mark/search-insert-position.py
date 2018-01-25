#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    【思路】
    根据题设：return the index if the target is found. If not, return the index ... assume no duplicates in the array.
    可知，我们直接二分法查找然后靠左（X 其实是靠右，大的那个）就行了。不用担心我们的算法在：
    [1, 2, 5, 5, 6] 中查找5的情况下出来的是：2还是3。
    """
    def searchInsert_0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, tail = 0, len(nums)
        while start != tail:
            half = (start + tail)/2
            if target == nums[half]:
                return half
            if target <= nums[half]:
                tail = half
            else:
                start = half + 1
        return start


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        这个算法NB在，不仅少了2行，还是Binary Search that handles duplicate
        详见最后一个test case
        """
        start, tail = 0, len(nums)
        while start != tail:
            half = (start + tail)/2
            if target > nums[half]:
                start = half + 1
            else:
                tail = half
        return start

if "__main__" == __name__:
    s = Solution()
    print s.searchInsert([1, 3, 5, 6], 0)  # 0
    print s.searchInsert([1, 3, 5, 6], 1)  # 0
    print s.searchInsert([1, 3, 5, 6], 2)  # 1
    print s.searchInsert([1, 3, 5, 6], 3)  # 1
    print s.searchInsert([1, 3, 5, 6], 4)  # 2
    print s.searchInsert([1, 3, 5, 6], 5)  # 2
    print s.searchInsert([1, 3, 5, 6], 6)  # 3
    print s.searchInsert([1, 3, 5, 6], 7)  # 4


    print s.searchInsert([1, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6], 5)  # 2
