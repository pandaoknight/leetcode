# -*- coding: utf-8 -*-
# description: 要求in-place地移动0
# 可以不用双指针，直接一趟可以搞定，保存0的计数。
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        count = 0
        curr = 0
        while curr < length:
            temp = nums[curr]
            if temp and count:
                nums[curr - count] = nums[curr]
                nums[curr] = 0
            if 0 == temp:
                count += 1
            curr += 1

if "__main__" == __name__:
    s = Solution()
    nums = [2, 1, 0]
    s.moveZeroes(nums)
    print nums
    print "[2, 1, 0] is expected"

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print nums
    print "[1, 3, 12, 0, 0] is expected"

    nums = [0, 1, 0, 3, 12, 0, 0]
    s.moveZeroes(nums)
    print nums
    print "[1, 3, 12, 0, 0, 0, 0] is expected"
