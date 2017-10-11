#!/usr/bin/python
# -*- coding:utf-8 -*-
# Input:
#[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
#Output:
#[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        s = sorted(people, cmp=lambda x,y:y[0]-x[0] if y[0]-x[0] else x[1]-y[1])
        que = []
        for i in s:
            que.insert(i[1], i)
        return que

if "__main__" == __name__:
    s = Solution()
    print s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
