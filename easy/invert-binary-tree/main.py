# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if "__main__" == __name__:
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    s = Solution()
    s.invertTree(root)
    print root.val
    print root.left.val
    print root.right.val
    print root.right.left.val
