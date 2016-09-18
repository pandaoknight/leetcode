#!/usr/bin/python
# -*- encoding: utf-8 -*-
class Solution(object):
    def binarySearch(self, needle, numbers):
        """
        :type needle: int
        :type numbers: List[int]
        # :type showSearchCount: boolean
        :rtype: List[found,before,after,searchCount]
        """
        searchCount = 0
        if needle == numbers[0]:
            return [0, None, 1, searchCount]
        if needle < numbers[0]:
            return [None, None, 0, searchCount]
        last = len(numbers) - 1
        if needle == numbers[last]:
            return [last, last-1, None, searchCount]
        if needle > numbers[-1]:
            return [None, last, None, searchCount]

        before, after = 0, last
        while before + 1 != after:
            searchCount += 1
            mid = (before + after) / 2
            if needle == numbers[mid]:
                return [mid, mid-1, mid+1, searchCount]
            if needle < numbers[mid]:
                after = mid
            else:
                before = mid
        return [None, before, after, searchCount]

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        found, before, after, searchCount = self.binarySearch(target / 2.0, numbers)
        #beforeList = numbers[before::-1]
        #afterList = numbers[after:]
        #print beforeList, afterList
        print "--start--"
        print numbers, target
        print found, before, after, searchCount
        if None != found:
            if None != after and numbers[found] == numbers[after]:
                # trans to not zero-based.
                return [found + 1, after + 1]
            if None != before and numbers[before] == numbers[found]:
                # trans to not zero-based.
                return [before + 1, found + 1]
        while -1 != before or len(numbers) != after:
            if target == numbers[before] + numbers[after]:
                break;
            if target < numbers[before] + numbers[after]:
                before -= 1
            else:
                after += 1
        # trans to not zero-based.
        return [before + 1, after + 1]


if "__main__" == __name__:
    # 测试二分查找
    numbers = [2, 7, 11, 15, 18, 19, 20, 21, 22, 34, 35, 60]
    s = Solution()
    '''
    print s.binarySearch(1, numbers) # None None 0
    print s.binarySearch(2, numbers) # 0
    print s.binarySearch(3, numbers) # None 0 1
    print s.binarySearch(7, numbers) # 1
    print s.binarySearch(11, numbers) # 2
    print s.binarySearch(12, numbers) # None 3 4
    print s.binarySearch(15, numbers) # 3
    print s.binarySearch(19, numbers) # 5
    print s.binarySearch(20, numbers) # 6
    print s.binarySearch(22, numbers) # 8
    print s.binarySearch(23, numbers) # None 8 9
    print s.binarySearch(33, numbers) # None 8 9
    print s.binarySearch(34, numbers) # 9
    print s.binarySearch(35, numbers) # 10
    print s.binarySearch(100, numbers) # None 10 None
    '''

    # 测试
    target = 9
    print s.twoSum(numbers, target)
    target = 28
    print s.twoSum(numbers, target)
    target = 30 # 11 19
    print s.twoSum(numbers, target)
    target = 37 # 15 22
    print s.twoSum(numbers, target)
    target = 38
    print s.twoSum(numbers, target)
    target = 62 # 2 60
    print s.twoSum(numbers, target)
    numbers = [1, 1]
    target = 2
    print s.twoSum(numbers, target)
    numbers = [1, 2, 2, 3] # 这两种情况很不好处理
    target = 4
    print s.twoSum(numbers, target) # 主要是因为
    numbers = [1, 2, 2, 3, 3]
    target = 4
    print s.twoSum(numbers, target)
