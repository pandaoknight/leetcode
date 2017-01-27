#!/usr/bin/python
# -*- encoding: utf-8 -*-

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        fir = {}
        sec = {}
        for i, c in enumerate(s):
            #print i, c
            if None != sec.get(c):
                continue
            if None == fir.get(c):
                fir[c] = i
            else:
                sec[c] = fir.pop(c)
        #print fir, sec
        #print min(fir)
        if fir:
            #return fir[min(fir)]
            return min(fir.values())
        return -1

if "__main__" == __name__:
    s = Solution()
    print s.firstUniqChar("leetcode")  # 0
    print s.firstUniqChar("loveleetcode")  # 2
    print s.firstUniqChar("ll")  # -1
    print s.firstUniqChar("bilibili")  # -1
    print s.firstUniqChar("aaaaab")  # 5
