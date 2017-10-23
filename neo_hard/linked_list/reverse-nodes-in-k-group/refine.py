#!/usr/bin/python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, n = None):
        self.val = x
        self.next = n

    def __str__(self):
        cur = self
        s = "%s" % cur.val
        while cur.next:
            cur = cur.next
            s += "->%s" % cur.val
        return s

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if 1 == k or None == head:
            return head

        # define a fake head
        fh = ListNode(None)
        fh.next = head
        # define 4 cursor and 1 counter for k
        gc = head  # gc:group-cursor
        ocr = head  # ocr:operating-cursor-for-reversing
        ocl = fh  # orl:operating-cursor-for-last-group
        ocls = None # orls:operating-cursor-for-last-group-start-mark
        count = 0
        while gc:
            if 0 == count % k:
                ocls = gc
            gc = gc.next
            count += 1
            if 0 == count % k:
                tmp = ocr.next
                ocr.next = gc
                last = ocr
                ocr = tmp
                for i in range(k - 2):
                    tmp = ocr.next
                    ocr.next = last
                    last = ocr
                    ocr = tmp
                ocl.next = ocr
                ocr.next = last
                ocr = gc
                ocl = ocls
        return fh.next

if "__main__" == __name__:
    s = Solution()
    print ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 6)
    print s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1)

    print s.reverseKGroup(ListNode(1, ListNode(2)), 2)
    print s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2)

    print s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
    print s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3)
    print s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5)
