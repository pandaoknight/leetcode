# -*- coding: utf-8 -*-
# description: 单词的模式判断
# Leetcode给他打的tag是：hash table，但我会直接利用python的dict。
#
# 对于长度不等做处理，对于空串进行考虑，都是空串的情况下是能过的。
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.strip().split()
        if len(pattern) != len(words):
            return False
        c2word = {}
        for i, c in enumerate(pattern):
            if not c2word.get(c, False):
                # words[i] must not in dict's values
                if words[i] in c2word.values():
                    return False
                c2word[c] = words[i]
            else:
                if c2word[c] != words[i]:
                    return False
        return True

if "__main__" == __name__:
    s = Solution()

    # not equal
    pattern = "abba"
    str = "dog cat"
    print pattern
    print str
    print s.wordPattern(pattern, str)
    print "False is expected."

    # not equal with empty
    pattern = ""
    str = "dog cat cat dog"
    print pattern
    print str
    print s.wordPattern(pattern, str)
    print "False is expected."

    # empty str
    pattern = ""
    str = ""
    print pattern
    print str
    print s.wordPattern(pattern, str)
    print "True is expected."


    pattern = "abba"
    str = "dog cat cat dog"
    print pattern
    print str
    print s.wordPattern(pattern, str)
    print "True is expected."

    pattern = "abba"
    str = "dog cat cat fish"
    print pattern
    print str
    print s.wordPattern(pattern, str)
    print "False is expected."

    pattern = "aaaa"
    str = "dog cat cat dog"
    print pattern
    print str
    print s.wordPattern(pattern, str)
    print "False is expected."

    pattern = "abba"
    str = "dog dog dog dog"
    print pattern
    print str
    print s.wordPattern(pattern, str)
    print "False is expected."
