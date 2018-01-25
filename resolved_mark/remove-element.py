#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeElement_0(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        head, tail = 0, len(nums)
        while True:
            while nums[tail - 1] == val and head < tail:
                tail -= 1
            while nums[head] != val and head < tail:
                head += 1
            if head >= tail:
                break
            nums[head], nums[tail - 1] = nums[tail - 1], nums[head]
        return tail

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, length = 0, len(nums)
        while i < length:
            if val == nums[i]:
                length -= 1
                nums[i] = nums[length]
            else:
                i += 1
        return length


if "__main__" == __name__:
    s = Solution()
    nums = [24, 2, 10, 8, 6, 4, 14]
    print s.removeElement(nums, 4)
    print nums