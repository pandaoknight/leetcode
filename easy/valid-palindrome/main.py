# -*- coding:utf-8 -*-
# description: 检查是不是回文
# 先处理空入参的情况，按题设要求返回True
# 1.移除所有的标点、空格
# 2.大小转小写，最后留下纯粹的小写字符串
# 知识点：
# 在Python中printable组成为：digits、letters、punctuation、whitespace。
# 那么我们这里要设置给 string.translate(s, table[, deletechars])的deletechars正是：punctuation+whitespace
import string, re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        lowered = s.lower()
        #deleted = lowered.translate(None, string.punctuation + string.whitespace)
        #table = string.maketrans("", "")
        #deleted = lowered.translate(table, string.punctuation + string.whitespace)
        regex = re.compile('[%s]' % re.escape(string.punctuation + string.whitespace))
        deleted = regex.sub('', lowered)
        #return deleted
        reversed = deleted[::-1]
        return deleted == reversed


if "__main__" == __name__:
    print "-*- test string enum -*-"
    print ',' in string.punctuation
    print ':' in string.punctuation
    print 'a' in string.punctuation
    print ' ' in string.punctuation
    print 'a' in string.letters
    print ' ' in string.whitespace
    print "-*- test string enum END -*-"
    s = Solution()
    print s.isPalindrome(None) # True
    print s.isPalindrome("") # True
    print s.isPalindrome(" ") # True
    print s.isPalindrome(" ;*") # True
    print s.isPalindrome("A man, a plan, a canal: Panama") # True
    print s.isPalindrome("race a car") # False
    print s.isPalindrome("rac a car") # True
    print s.isPalindrome("aA") # True
