# -*- coding: utf-8 -*-
# Problem Description:
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
#
# Examples:
#
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# Notes:
# You may assume both pattern and str contains only lowercase letters.
#
# description: 单词的模式判断（II型）
# 这题竟然是付费的。。。确实比"单词的模式判断"那题要难的多。
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
