class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # sys.maxint = 9223372036854775807
        # -sys.maxint - 1 = -9223372036854775808
        #
        if 0 == x:
            return 0
        negtive_flag = False
        if 0 > x:
            x = abs(x)
            negtive_flag = True

        result = 0
        while x:
            x, remainder = divmod(x, 10)
            #print x, remainder
            result = 10*result + remainder
            #print result

        if negtive_flag:
            result *= -1
        if 2147483647 < result or -2147483648 > result:
            return 0

        if type(result) is not int:
            return 0
        return result

if "__main__" == __name__:
    s = Solution()
    print s.reverse(0)
    print s.reverse(123)
    print s.reverse(-123)
    print s.reverse(1230000000)
    print s.reverse(-1230000000)
    print s.reverse(123001000)
    print s.reverse(9223372036854775807)
    print s.reverse(7085774586302733239)

    print s.reverse(1534236469)
    print s.reverse(2147483648)
    print s.reverse(-2147483648)
    print s.reverse(7463847412)
    print s.reverse(8463847412)
    print s.reverse(-8463847412)
    print s.reverse(-9463847412)
