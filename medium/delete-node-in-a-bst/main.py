# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        #0 find the key
        if root is None:
            return None

        #0 special situation
        if key == root.val and root.right is None and root.left is None:
            return None

        #
        last = None
        #last_direction = None
        cur = root
        #1 Not found
        while cur:
            if key == cur.val:
                break
            last = cur
            if key > cur.val:
                cur = cur.right
                continue
            if key < cur.val:
                cur = cur.left
                continue
        if cur is None:
            return root

        #2 leaf remove
        if cur.left is None and cur.right is None:
            if key > last.val:
                last.right = None
            else:
                last.left = None
            return root

        #3 node remove, by "right smallest replace"
        if cur.right is None:
            #3.1 only has left, must replace a node
            cur.val = cur.left.val # remember always operate the value first
            cur.right = cur.left.right
            cur.left = cur.left.left
            return root

        if cur.right is not None and cur.right.left is None:
            #3.2 right has no left, must replace a node
            cur.val = cur.right.val
            cur.right = cur.right.right
            return root

        if cur.right is not None and cur.right.left is not None:
            cur_s = cur.right.left
            last_s = cur.right
            while cur_s.left is not None:
                last_s = cur_s
                cur_s = cur_s.left

            if cur_s.right is not None:
                #3.3 replace 2 node, (may not) delete the leaf
                cur.val = cur_s.val
                cur_s.val = cur_s.right.val
                cur_s.left = cur_s.right.left
                cur_s.right = cur_s.right.right # remember always operate the changed node last
                return root

            if cur_s.right is None:
                #3.4 replace 1 node, delete the leaf
                cur.val = cur_s.val
                last_s.left = None
                return root

        # never delete root, but change val.
        return root

