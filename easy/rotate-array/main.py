class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        new = nums[-k:]+nums[:-k]
        #return nums
        for i,v in enumerate(new):
            nums[i] = v


if "__main__" == __name__:
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    print s.rotate(nums, 3)
    print nums

    nums = [1]
    print s.rotate(nums, 0)
    print nums

    nums = [1,2]
    print s.rotate(nums, 3)
    print nums
