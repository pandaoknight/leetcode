class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        other_map = {}
        for i in range(len(s)):
            if t[i] != map.get(s[i], t[i]) or s[i] != other_map.get(t[i], s[i]):
                return False
            else:
                map[ s[i] ] = t[i]
                other_map[ t[i] ] = s[i]
        #print map
        #print other_map
        return True

if "__main__" == __name__:
    s = Solution()
    print s.isIsomorphic("egg", "add")
    print s.isIsomorphic("egg", "adc")
    print s.isIsomorphic("ab", "aa")
    print s.isIsomorphic("foo", "bar")
    print s.isIsomorphic("foq", "baa")
