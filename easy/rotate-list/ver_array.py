#!/usr/bin/python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def show(self):
        cur = self
        while(None != cur):
            print cur.val
            cur = cur.next
        print "END!!"

#import Queue

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if None == head or None == head.next or 0 == k:
            return head

        array = []
        while head:
            array.append(head)
            head = head.next
        k = k % len(array)
        if 0 == k:
            return array[0]
        array[-k - 1].next = None
        array[-1].next = array[0]
        return array[-k]


if "__main__" == __name__:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    #head = ListNode(1)
    #head.show()

    s = Solution()
    s.rotateRight(head, 2000000001).show();
