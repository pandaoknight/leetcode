class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        target = self.stack.pop()
        if target == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1] if self.stack else None


if "__main__" == __name__:
    s = MinStack()
    s.push(9)
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.push(6)
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.push(7)
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.push(6)
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.push(5)
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.push(0)
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.pop()
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.pop()
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.pop()
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.push(3)
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.pop()
    print s.stack
    print s.top()
    print s.getMin()
    print ""
    s.pop()
    print s.stack
    print s.top()
    print s.getMin()
    s.pop()
    print s.stack
    print s.top()
    print s.getMin()
    s.pop()
    print s.stack
    print s.top()
    print s.getMin()
    print ""
