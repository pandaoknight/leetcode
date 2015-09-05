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
        if None == head or 0 == k:
            return head

        cur = head
        tail = head
        i = 0
        while i < k:
        #for i in range(0, k):
            #print "i: %s" % i
            if None != cur.next:
                cur = cur.next
            else:
                size = i + 1
                #print "size: %s" % size
                return self.rotateRight(head, k % size)
            i += 1

        while(None != cur.next):
            tail = tail.next
            cur = cur.next
        new_head = tail.next
        tail.next = None
        cur.next = head
        return new_head


if "__main__" == __name__:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    #head = ListNode(1)
    #head.show()

    s = Solution()
    s.rotateRight(head, 2000000001).show();
