# -*- coding: utf-8 -*-
# description: 括号闭环判断（valid-parenthese）
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {"}":"{", "]":"[", ")":"("}
        for c in s:
            #print stack
            if c in "({[":
                stack.append(c)
            if c in ")}]":
                if not stack or map[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack

if "__main__" == __name__:
    s = Solution()

    str = "()"
    print str
    print s.isValid(str)
    print "True is expected."

    str = "(){}[]"
    print str
    print s.isValid(str)
    print "True is expected."

    str = "(]"
    print str
    print s.isValid(str)
    print "False is expected."

    str = "([)]"
    print str
    print s.isValid(str)
    print "False is expected."

    str = "((())"
    print str
    print s.isValid(str)
    print "False is expected."
