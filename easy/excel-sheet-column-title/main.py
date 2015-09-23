class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if 0 == n:
            return ''
        result = []
        q, r = divmod(n-1, 26)
        while q:
            result.insert(0, chr(ord('A')+r))
            q, r = divmod(q-1, 26)
        result.insert(0, chr(ord('A')+r))
        return "".join(result)


if "__main__" == __name__:
    s = Solution()
    print s.convertToTitle(1) #A
    print s.convertToTitle(0) #NULL
    print s.convertToTitle(10) #J
    print s.convertToTitle(26) #Z
    print s.convertToTitle(27) #AA = 26+1
    print s.convertToTitle(53) #BA = AA+26
    print s.convertToTitle(52) #AZ = AA+25 = 26+26
    print s.convertToTitle(702) #ZZ = AZ+25*26 = 26+26^2
    print s.convertToTitle(703) #AAA = AZ+25*26 = 26+26^2+1
    print s.convertToTitle(18278) #ZZZ = 26+26^2+26^3
    print s.convertToTitle(18279) #AAAA = 26+26^2+26^3+1
