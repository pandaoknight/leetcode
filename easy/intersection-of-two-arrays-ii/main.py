# -*- coding: utf-8 -*-
# description: 取列表的交集，题设中输出对于顺序没有要求。
# 解决思路：使用dict结构，做计数。一趟解决问题，o(n)。

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        inter = []
        for num in nums2:
            count = dict1.get(num, 0)
            if count:
                inter.append(num)
                dict1[num] = count -1
        return inter


if "__main__" == __name__:
    s = Solution()
    print s.intersect([1, 2, 2, 1], [2, 2])
