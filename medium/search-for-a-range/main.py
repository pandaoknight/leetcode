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
        start = 0
        end = len(nums) - 1
        middle = (start+end)/2
        while start < end or target != nums[middle]:
            if target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
            middle = (start+end)/2
        if start >= end and target != nums[start]:
            return [-1, -1]
        return None
        #2 find start
        mid4start = (start+middle)/2
        while start != mid4start:
            pass
        #3 find end
        mid4end = (end+middle)/2
        while true:
            if target != nums[mid4end]:
                end = mid4end
        return [start, end]

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
    print s.searchRange(nums, 8) # 3,4
    print s.searchRange(nums, 7) # 1,2
    print s.searchRange(nums, 10) # 5,5
    print s.searchRange(nums, 5) # 0,0
    print s.searchRange(nums, 3) # -1,-1
    print s.searchRange(nums, 11) # -1,-1
    print s.searchRange(nums, 6) # -1,-1
    print s.searchRange(nums, 9) # -1,-1
