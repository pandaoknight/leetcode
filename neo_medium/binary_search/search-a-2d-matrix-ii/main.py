#!/usr/bin/python
#-*- coding: utf-8 -*-
# description: 在一个X、Y轴上都单调递增的二位矩阵里面检索一个值是否确切存在。
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        return self.recurSearchMatrix(matrix, 0, len(matrix[0]), 0, len(matrix), target)

    def recurSearchMatrix(self, matrix, xs, xe, ys, ye, target):
        print "------------- Search %d ----------------" % target;
        print xs, xe, ys, ye
        size = min(xe - xs, ye - ys)
        if 0 == size:
            return False
        ss, se = 0, size
        mid = (ss + se) / 2
        if target == matrix[ys][xs]:
            return True
        elif target < matrix[ys][xs]:
            return False
        while ss != mid:
            midValue = matrix[ys + mid][xs + mid]
            print midValue
            if midValue == target:
                return True
            elif midValue < target:
                ss = mid
                mid = (mid + se) / 2
            else:
                se = mid
                mid = (ss + mid) / 2
        print ss
        if self.recurSearchMatrix(matrix, xs, xs + ss + 1, ys + ss + 1, ye, target):
            return True
        if self.recurSearchMatrix(matrix, xs + ss + 1, xe, ys, ys + ss + 1, target):
            return True

        return False

if "__main__" == __name__:
    matrix = [
               [1,   4,  7, 11, 15],
               [2,   5,  8, 12, 19],
               [3,   6,  9, 16, 22],
               [10, 13, 14, 17, 24],
               [18, 21, 23, 26, 30]
             ]
    matrix = [
               [1,   4,  7, 11, 15],
               [2,   5,  8, 12, 19],
               [3,   6,  9, 16, 22],
               [5, 13, 14, 17, 24],
               [6, 21, 23, 26, 30]
             ]
    s = Solution()
    print s.searchMatrix(matrix, 5)
    print s.searchMatrix(matrix, 6)
    print s.searchMatrix(matrix, 1)
    print s.searchMatrix(matrix, 0)
    print s.searchMatrix(matrix, 30)
    print s.searchMatrix(matrix, 31)
    print s.searchMatrix(matrix, 18)
