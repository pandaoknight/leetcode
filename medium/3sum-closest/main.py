class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        ret = sum(nums[0:3])
        dif = abs(ret - target)
        for i in range(1, len(nums) - 2):
            tmp = sum(nums[i:i+3])
            if dif > abs(tmp - target):
                dif = abs(tmp - target)
                ret = tmp
        return ret

nums = [-1, 2, -100, -4, 5, 6, -10, 11, 20, 12]
target = 1
s = Solution()
c = s.threeSumClosest(nums, target)
print c
