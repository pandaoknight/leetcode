#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'PC'

class Solution(object):
    """
    【思路】
    这是一个典型的 an=f(n,a1,a2)的函数，所以只要进行a1,a2的可能性遍历就行了。
    假设总长是: l
    1. 设立a1，a2两个游标，组合从(1,1)开始到直到(m,n)
    2. 如果: l < max(m, n) 那么就可以结束了，因为位数不够了，不用比大小了
    *3. 这个题在判断an是不是合规*的时候，不要用尾递归，直接用循环
    4. 对于a3而言，把剩余的串一个一个pop出来，进行比对，合规则比a4。以此类推。
    *4.1 一个优化是，看剩余的串是不是已经比an短了，如果短则没有必要比较
    *4.2 获取an可以使用Python的yield
    5. 当要取an+1进行比对的时候，如果这时串正好一个不剩。那么，说明整个串是合规**的。

    6. 如果不合规，则令a2先增大
    *7. 注意需要对a1,a2进行合规***校验，见题目Note：
    Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
    *7.1 后面的数字是不需要进行合规校验的，因为如果起首为0，则肯定不匹配。
    """
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l = len(num)
        if l == 0:
            return True
        if l == 1:
            return True
        if l == 2:
            return True
        for m in range(1, l/2 + 1):
            n = 1
            while l-m-n >= max(m, n):
                print "m: %s n: %s" % (m, n)
                a1 = num[:m]
                a2 = num[m:m+n]
                remained = num[m+n:]
                #
                n += 1
                if False == self.notZeroLeading(a1) or False == self.notZeroLeading(a2):
                    continue

                print "a1: %s a2: %s" % (a1, a2)
                gen = self.fib(int(a1), int(a2))
                while True:
                    an = str(gen.next())
                    print "an: %s" % an
                    if len(an) > len(remained):
                        break
                    split = remained[:len(an)]
                    remained = remained[len(an):]
                    print "split: %s remained %s" % (split, remained)
                    if an != split:
                        break
                    # Exit
                    if "" == remained:
                        return True
        return False

    def fib(self, a, b):
        while True:
            a, b = b, a + b
            yield b

    def notZeroLeading(self, a):
        if "0" == a:
            return True
        if "0" == a[0]:
            return False
        else:
            return True

if "__main__" == __name__:
    s = Solution()
    ## Function Unit-test
    print "fib unit-test"
    gen = s.fib(1, 2)
    print gen.next()  # 3
    print gen.next()  # 5
    print gen.next()  # 8


    print "notZeroLeaing unit-test"
    print s.notZeroLeading("0")  # True
    print s.notZeroLeading("01")  # False
    print s.notZeroLeading("10")  # True

    ## Solution Test
    print "solution test"
    print s.isAdditiveNumber("")  # True?
    print s.isAdditiveNumber("0")  # True?
    print s.isAdditiveNumber("1")  # True?

    print s.isAdditiveNumber("01")  # True
    print s.isAdditiveNumber("00")  # True
    print s.isAdditiveNumber("011")  # True

    print s.isAdditiveNumber("112")  # True
    print s.isAdditiveNumber("1123")  # True
    print s.isAdditiveNumber("112358")  # True
    print "1123581321"
    print s.isAdditiveNumber("1123581321")  # True
    print s.isAdditiveNumber("11235813211")  # False
    print s.isAdditiveNumber("112358132")  # False
    print s.isAdditiveNumber("11235813021")  # False


    print "1123581321345589144"
    print s.isAdditiveNumber("1123581321345589144")  # True
    print s.isAdditiveNumber("1123581321345589145")  # False
    print s.isAdditiveNumber("112358132134558914")  # False
    print s.isAdditiveNumber("11235813213455891444")  # False

    print "1023 ..."
    print s.isAdditiveNumber("1023")  # False
    print s.isAdditiveNumber("1203")  # False

    print "112334"
    print s.isAdditiveNumber("112334")  # True
    print s.isAdditiveNumber("11233457")  # True
    print s.isAdditiveNumber("11233458")  # False
    print s.isAdditiveNumber("11233459")  # False
