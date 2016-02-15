# -*- coding:utf-8 -*-
# description: 没有进大头，主要的性能问题是：自己从右边反查即可。不需要整个串都遍历。
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtrimmed = s.rstrip()
        if not rtrimmed:
            return 0
        return len(rtrimmed) - (rtrimmed.rfind(' ') + 1)

if "__main__" == __name__:
    s = Solution()
    print s.lengthOfLastWord("Hello world  ") # 5
    print s.lengthOfLastWord("Helloooooooooooo world  ") # 5
    print s.lengthOfLastWord("  ") # 0
    print s.lengthOfLastWord("abc ") # 3
    print s.lengthOfLastWord(" abc ") # 3
    print s.lengthOfLastWord("  abc ") # 3
