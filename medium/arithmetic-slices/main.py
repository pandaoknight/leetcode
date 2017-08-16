#!/usr/bin/python
#-*- coding:utf-8 -*-
# Definition for a binary tree node.

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        if 3 > l:
            return 0
        diff = A[1] - A[0]
        sub_l = 0
        total = 0
        for i in range(2, l):
            if diff == A[i] - A[i-1]:
                sub_l += 1
            else:
                total += self.triangularNumber(sub_l)
                sub_l = 0
                diff = A[i] - A[i-1]
        total += self.triangularNumber(sub_l)
        return total

    def triangularNumber(self,n):
        return (n+1)*n/2

if "__main__" == __name__:
    print "中文"
    s = Solution()
    print s.numberOfArithmeticSlices([])  # 0
    print s.numberOfArithmeticSlices([1])  # 0
    print s.numberOfArithmeticSlices([1,2])  # 0
    print s.numberOfArithmeticSlices([1,2,3])  # 1
    print s.numberOfArithmeticSlices([1,2,3,4])  # 3
    print s.numberOfArithmeticSlices([1,2,3,4,5])  # 6
    print s.numberOfArithmeticSlices([1,2,3,4,5,6])  # 10
    print s.numberOfArithmeticSlices([1,2,3,4,5,6,8])  # 10
    print s.numberOfArithmeticSlices([1,2,3,4,5,6,8,10])  # 11
