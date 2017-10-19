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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        m = max(1, m)
        if m >= n:
            return head
        fake_head = ListNode(0)
        fake_head.next = head
        # init
        count, cur, before_work = 1, head, fake_head
        # travel-loop
        while m != count:
            before_work = cur
            cur = cur.next
            count += 1
        tail_work = cur
        # work-loop
        before = None
        while n >= count and cur:
            next_tmp = cur.next
            ##
            cur.next = before
            before = cur
            #
            cur = next_tmp
            count += 1
        # link the before_work
        before_work.next = before
        # link the tail
        tail_work.next = cur
        return fake_head.next

if "__main__" == __name__:
    s = Solution()
    print ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 6)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 2)
    print ""
    print s.reverseBetween(ListNode(1, ListNode(2)), 2, 2)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2, 2)
    print ""
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 3)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3, 4)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5, 5)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5, 6)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 4, 5)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 5)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 4)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 3)
    print s.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)
