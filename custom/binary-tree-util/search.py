# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



if "__main__" == __name__:
    valList = xrange(2, 200)
    root = TreeNode(1)
    nodeList = [root]
    current = None
    for i in valList:
        if not current or current.right:
            current = nodeList.pop(0)
            current.left = TreeNode(i)
            nodeList.append(current.left)
        else:
            current.right = TreeNode(i)
            nodeList.append(current.right)

    levelTravel = [root]
    while levelTravel:
        current = levelTravel.pop(0)
        if current.left:
            levelTravel.append(current.left)
        if current.right:
            levelTravel.append(current.right)
        print current.val
