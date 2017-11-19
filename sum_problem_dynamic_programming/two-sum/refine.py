#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    【思路】
    1. 之前的思路是从中间开始往两边找。这确实是完备的。
    2. 那么现在我在解3Sum时突然开窍的是，我们从两头开始找，可以每次缩小检索范围。这样原本一个NlogN复杂度的算法，因为N在不断缩小，实际值要小得多。
    3. 那么具体的做法是，先从[0]开始，二分查找target-[0]，这一步是logN的。
    4. 然后，假设在[n-1]中找到了[m] == target-[0] 则这是一个candidate。否则，令[m] < target-[0] < [m+1]的情况成立。
    5. 此时，你的candidate范围已经缩小到[1]和[m]之间。因为对于[m] == target-[0]要判断[0][1]是否相等的情况，其实我觉得这个地方题设巨特么SB。
    6. 那么，在[1]到[m]之间，我们可以这次排除[m]而不是排除[1]，似乎这可能更容易更快地衰减N。但实际上是这样的，|[0]-[1]|和|[m]-[m+1]|谁大，先排除谁令N衰减地快。当整个数列分布地很均匀的时候，用二分查找乘以了logN倍的查找时间。
    7. 上面这个方案显然不是最优解。
    8. 一个我能想到的最优解，有一点类似于建立一个二叉搜索树。我们知道一个顺序列表（去重后），可以直接通过不断二分建立一个最矮的BST，它一定是平衡的，注意最矮和平衡是不同的要求，均匀二叉树，是要求最高的。
    9. 但实际上，我要建立的检索还要更夸张一些，它实际上是二分再二分，形成很多个匹配块儿。会使用递归，让我们的栈里面，至多保留logN份变量。
    10. 简单地来说是这样的：A已经去重，将A按target/2分为左右两部分。A[1~M]和A[M+1~N]，如果左边的A[1~M]数量少，则把A[1~M]分成3部分。为A[1~m-1]、A[m]、A[m+1~M]，如果A[m]匹配了，这就已经是一个candidate了。如果没有，则把A[M+1~N]分作两个部分，用来匹配前面剩余的两个部分。

    *11. 注意，这个算法当我们做3Sum的时候，是必定要用到"未去重"的列表的，例如：我们要得到一个[-12, +6, +6]的candidate。在4Sum中更是如此。
    """
    def twoSum(self, nums, target):
        """
        :type nums: Listint]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return None
        #print "=============================="
        # Special procecess for the requirement
        num_to_index = {}
        num_to_index_duplicated = {}
        for index, num in enumerate(nums):
            if num_to_index.has_key(num):
                tmp = num_to_index_duplicated.get(num, [])
                tmp.append(index)
                num_to_index_duplicated[num] = tmp
                ##
                #if num_to_index_duplicated.has_key(num):
                #    num_to_index_duplicated[num].append(index)
                #else:
                #    num_to_index_duplicated[num] = [index]
            else:
                num_to_index[num] = index
        for key in num_to_index_duplicated:
            num_to_index_duplicated[key].insert(0, num_to_index[key])
            del num_to_index[key]
        #print nums
        #print num_to_index
        #print num_to_index_duplicated

        # Middle special candidate
        if num_to_index_duplicated.has_key(target/2.0):
            return num_to_index_duplicated[target/2.0]

        # Recursive solution
        sorted_nums = sorted(num_to_index)
        index, nums_left, nums_right = self.sortedListBinarySplit(sorted_nums, target/2.0)

        self.target = target
        candidate = self.recur(nums_left, nums_right)
        if None == candidate:
            return None

        return map(lambda x:num_to_index[x], candidate)

    def recur(self, nums_left, nums_right):
        """
        :type nums_left: list[int]
        :type nums_right: list[int]
        :rtype cadidate: None or list[int]

        Predefinetion of self.target is required.
        """
        if not nums_left or not nums_right:
            return None

        nums_small, nums_big = (nums_left, nums_right) if len(nums_left) < len(nums_right) else (nums_right, nums_left)
            
        left = nums_small[len(nums_small)/2]
        index, nums_big_left, nums_big_right = self.sortedListBinarySplit(nums_big, self.target - left)
        if None != index:
            return [left, nums_big[index] ]
        # left recur and right recur
        left_candidate = self.recur(nums_small[:len(nums_small)/2], nums_big_right)
        if None != left_candidate:
            return left_candidate
        right_candidate = self.recur(nums_small[len(nums_small)/2+1:], nums_big_left)
        if None != right_candidate:
            return right_candidate

        return None

    def sortedListBinarySplit(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype index: None or int
        :rtype lnums: list[int]
        :rtype rnums: list[int]
        """
        if nums[0] >= target:
            if nums[0] == target:
                return 0, [], nums[1:]
            else:
                return None, [], nums
        if nums[-1] <= target:
            if nums[-1] == target:
                return len(nums)-1, nums[:-1], []
            else:
                return None, nums, []

        l, r = 0, len(nums)-1
        while l+1 != r:
            m = (l+r)/2
            if nums[m] == target:
                return m, nums[:m], nums[m+1:]
            if nums[m] > target:
                r = m
            else:
                l = m
        index, lnums, rnums = None, nums[:r], nums[r:]
        return index, lnums, rnums

if "__main__" == __name__:
    test_s = Solution()
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 0)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 16)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 2)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 15)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 7)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 8)
    print test_s.sortedListBinarySplit([2, 3, 7 ,11, 15], 11)



    s = Solution()
    print s.twoSum([2, 7], 9)
    print s.twoSum([2, 7 ,11, 15], 9)
    print s.twoSum([2, 7 ,11, 15], 22)
    print s.twoSum([2, 3, 7 ,11, 15], 14)
    print s.twoSum([2, 3, 7 ,11, 15], 15)

    print s.twoSum([3, 3], 6)
    print s.twoSum([2, 3, 7, 7, 11, 15], 14)
    print s.twoSum([2, 3, 4, 7, 7, 11, 15], 14)
