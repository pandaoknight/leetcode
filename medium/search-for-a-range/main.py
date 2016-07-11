# -*- coding: utf-8 -*-
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        #1 find one
        start = -1
        end = len(nums)
        middle = (start+end)/2
        while target != nums[middle]:
            if target < nums[middle]: # 比当前小的话只有一种情况结束
                end = middle
            else:
                start = middle
            if start+1 == end: # 最后都可以在这个阶段收束成一种情况来判断
                return [-1, -1]
                break
            middle = (start+end)/2
        #return middle # 至此这是一个标准的二分查找

        #2 find start
        end4start = middle
        mid = (start+end4start+1)/2 # 这样保证我取到的是ceil
        while start != (end4start - 1):
            if target == nums[mid]:
                end4start = mid
            else:
                start = mid
            mid = (start+end4start+1)/2

        #3 find end
        start4end = middle
        mid = (start4end+end)/2 # 这样保证我取到的是ceil
        while start4end != (end - 1):
            if target == nums[mid]:
                start4end = mid
            else:
                end = mid
            mid = (start4end+end)/2
        return [end4start, start4end]

if "__main__" == __name__:
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    print s.searchRange(nums, 8) # 3,4
    print s.searchRange(nums, 7) # 1,2
    print s.searchRange(nums, 10) # 5,5
    print s.searchRange(nums, 5) # 0,0
    print s.searchRange(nums, 3) # -1,-1
    print s.searchRange(nums, 11) # -1,-1
    print s.searchRange(nums, 6) # -1,-1
    print s.searchRange(nums, 9) # -1,-1
    nums = [5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 8, 8, 10]
    print s.searchRange(nums, 8) # 11,12
    print s.searchRange(nums, 7) # 4,10
    print s.searchRange(nums, 10) # 13,13
    print s.searchRange(nums, 5) # 0,3
    print s.searchRange(nums, 3) # -1,-1
    print s.searchRange(nums, 11) # -1,-1
    print s.searchRange(nums, 6) # -1,-1
    print s.searchRange(nums, 9) # -1,-1
