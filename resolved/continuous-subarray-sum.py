#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Given a list of non-negative numbers and a target integer k,
    write a function to check if the array has a continuous subarray
    of size at least 2 that sums up to the multiple of k, that is,
    sums up to n*k where n is also an integer.

    【思路】
    一开始题读错了。它要求是K的倍数。这就麻烦了。因为不能用窗口加减法。但是取模是肯定要用到的。
    """
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            zero_flag = False
            for num in nums:
                if num == 0:
                    if zero_flag:
                        return True
                    zero_flag = True
                    continue
                zero_flag = False
            return False

        remainder2exist = {0: True,}
        remainder2exist[nums[0] % k] = True
        remainder = nums[0] % k
        for num in nums[1:]:
            remainder = (remainder + num) % k
            if remainder2exist.get(remainder):
                return True
            else:
                remainder2exist.setdefault(remainder, True)
        return False
if "__main__" == __name__:
    s = Solution()
    nums = [23, 2, 10, 8, 6, 4, 14]
    print s.checkSubarraySum(nums, 23)  # True
    print s.checkSubarraySum(nums, 10)  # True

    print s.checkSubarraySum(nums, 14)  # True
    print s.checkSubarraySum(nums, 25)  # True
    print s.checkSubarraySum(nums, 28)  # True

    print s.checkSubarraySum(nums, 15)  # False => True 15 *3 = 45 = 23+2+10+8
    print s.checkSubarraySum(nums, 29)  # False
    print s.checkSubarraySum(nums, 33)  # False
