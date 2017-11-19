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
        # build a dict is not high-cost, but list.index() is high cost
        #index_dict = xxx
        nums = map(lambda x:(x[1], x[0]), enumerate(nums))
        nums = sorted(nums)
        half = target / 2.0
        left_index, right_index = 0, len(nums) - 1
        while left_index != right_index - 1:
            mid_index = (left_index + right_index) / 2
            mid = nums[mid_index][0]
            if half == mid:
                if nums[mid_index][0] == nums[mid_index + 1][0]:
                    left_index = mid_index
                    right_index = mid_index + 1
                else:
                    left_index = mid_index - 1
                    right_index = mid_index
                break
            if half > mid:
                left_index = mid_index
            else:
                right_index = mid_index

        #print left_index, right_index

        while left_index >= 0 and right_index < len(nums):
            the_sum = nums[left_index][0] + nums[right_index][0]
            if target == the_sum:
                #return [ nums[left_index][0], nums[right_index][0] ]
                return [ nums[left_index][1], nums[right_index][1] ]
            if target > the_sum:
                right_index += 1
            else:
                left_index -= 1

        return None

if "__main__" == __name__:
    s = Solution()
    print s.twoSum([2, 7], 9)
    print s.twoSum([2, 7 ,11, 15], 9)
    print s.twoSum([2, 7 ,11, 15], 22)
    print s.twoSum([2, 3, 7 ,11, 15], 14)
    print s.twoSum([2, 3, 7 ,11, 15], 15)

    print s.twoSum([3, 3], 6)
    print s.twoSum([2, 3, 7, 7, 11, 15], 14)
    print s.twoSum([2, 3, 4, 7, 7, 11, 15], 14)
