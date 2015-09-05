class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.path = []
        self.paths = [] # list[str]
        self.recur(root)
        return self.paths

    def recur(self, node):
        #self.path.append(node.val) # if it is a PHP, there won't be any problems. PHPer has scant sense on Strongly-type.
        self.path.append(str(node.val))
        if node.left:
            self.recur(node.left)
        if node.right:
            self.recur(node.right)
        # After-order
        if not node.left and not node.right:
            self.paths.append("->".join(self.path))
        self.path.pop()

if "__main__" == __name__:
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    s = Solution()
    print s.binaryTreePaths(root)
