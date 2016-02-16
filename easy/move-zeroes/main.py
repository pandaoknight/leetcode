# -*- coding: utf-8 -*-
# description: 要求in-place地移动0
# 还是用双指针，一趟（好吧，实际上相当于2趟）完成
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        fast = 0
        slow = 0
        while fast < length:
            if nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < length:
            nums[slow] = 0
            slow += 1

if "__main__" == __name__:
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print nums
    print "[1, 3, 12, 0, 0] is expected"

    nums = [0, 1, 0, 3, 12, 0, 0]
    s.moveZeroes(nums)
    print nums
    print "[1, 3, 12, 0, 0, 0, 0] is expected"
