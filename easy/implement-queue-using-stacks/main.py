class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackIn = []
        self.stackOut = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stackIn.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self._in2out()
        if self.stackOut:
            return self.stackOut.pop()
        else:
            return None

    def peek(self):
        """
        :rtype: int
        """
        self._in2out()
        return self.stackOut[-1]

    def empty(self):
        """
        :rtype: bool
        """
        self._in2out()
        return 0 == len(self.stackOut)

    def _in2out(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())


if "__main__" == __name__:
    q = Queue()
    print q.empty()
    q.push(1)
    print q.peek() # 1
    print q.empty()
    q.push(2)
    print q.peek() # 1
    q.push(3)
    print q.pop()
    print q.peek() # 2
    print q.empty()
    q.push(4)
    q.push(5)
    print q.pop()
    print q.pop()
    print q.pop()
    print q.empty()
    print q.pop()
    print q.empty()
