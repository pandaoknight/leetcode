#!/usr/bin/python
#-*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sumDict = {}
        self.getFrequentTreeSumDict(root, sumDict)
        frequentDict ={}
        for key in sumDict:
            val = sumDict[key]
            item = frequentDict.get(val, [])
            item.append(key)
            frequentDict[val] = item
        #return frequentDict
        return frequentDict[max(frequentDict)]

    def getFrequentTreeSumDict(self, root, sumDict):
        if not root:
            return 0
        leftSum = self.getFrequentTreeSumDict(root.left, sumDict)
        rightSum = self.getFrequentTreeSumDict(root.right, sumDict)
        rootSum = root.val + leftSum + rightSum
        count = sumDict.get(rootSum, 0)
        sumDict[rootSum] = count + 1
        return rootSum
if "__main__" == __name__:
    s = Solution()

    root = TreeNode(1, TreeNode(2, TreeNode(5), TreeNode(1)), TreeNode(3, None, TreeNode(9)))
    print s.getFrequentTreeSumDict(root, {})
    print s.findFrequentTreeSum(root)

    root = TreeNode(5, TreeNode(2), TreeNode(-5))
    print s.getFrequentTreeSumDict(root, {})
    print s.findFrequentTreeSum(root)
