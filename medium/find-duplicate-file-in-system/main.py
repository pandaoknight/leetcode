#!/usr/bin/python
#-*- coding:utf-8 -*-
import re
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        fcp = re.compile("(.+)\((\w+)\)")  # fileContentPattern
        result = {}
        for path in paths:
            tmp = path.split(" ")
            rootPath = tmp.pop(0)
            #print rootPath,tmp
            for fc in tmp:
                #print fc
                m = fcp.match(fc)
                #print m
                fn = m.group(1)
                content = m.group(2)
                g = result.get(content)
                if None == g:
                    g = []
                    result[content] = g
                g.append(rootPath + "/" + fn)

        return filter(lambda x: len(x) > 1, result.values())
        #return result.values()

if "__main__" == __name__:
    print "中文"
    s = Solution()
    print s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
    print s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]) # 期望结果为[] 因为需要对只有一个元素的数组进行过滤
