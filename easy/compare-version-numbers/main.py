class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        for i in range(max(len(v1), len(v2))):
            try:
                d1 = int(v1[i])
            except:
                d1 = 0
            try:
                d2 = int(v2[i])
            except:
                d2 = 0
            if d1 > d2:
                return 1
            if d2 > d1:
                return -1
        return 0

# 0.1 < 1.1 < 1.2 < 13.37
if "__main__" == __name__:
    s = Solution()
    print s.compareVersion("1.5", "1.12") #-1
    print s.compareVersion("1.5", "1.5.1") #-1
    print s.compareVersion("1.5.1", "1.5") #1
    print s.compareVersion("1.5.0", "1.5") #0
    print s.compareVersion("1.5.0.0", "1.5") #0
    print s.compareVersion("1.5.0.1", "1.5") #1
