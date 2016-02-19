# -*- coding: utf-8 -*-
# description: 单列表重新组织成，奇数节点在前，偶数节点在后的列表。
# 使用 异或（is_odd ^= 1）来进行简单的翻转标记。
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def toList(self):
        curr = self
        list = []
        while curr:
            list.append(curr.val)
            curr = curr.next
        return list

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        even_head = head.next
        curr = head
        is_odd = 0

        odd_tail = False
        last = False
        last_second = False
        while curr:
            is_odd ^= 1
            if is_odd:
                odd_tail = curr
            if last_second:
                last_second.next = curr
            last_second = last
            last = curr
            curr = curr.next
        #if is_odd:
        #    last.next = None
        last_second.next = None
        odd_tail.next = even_head
        return head


if "__main__" == __name__:
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print head.toList()
    head = s.oddEvenList(head)
    print head.toList()
    print "1->3->5->2->4 is expected"

    head = ListNode(1)
    print head.toList()
    head = s.oddEvenList(head)
    print head.toList()
    print "1 is expected"

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print head.toList()
    head = s.oddEvenList(head)
    print head.toList()
    print "1->3->2->4 is expected"

    head = ListNode(1, ListNode(2, ListNode(3)))
    print head.toList()
    head = s.oddEvenList(head)
    print head.toList()
    print "1->3->2 is expected"

    head = ListNode(1, ListNode(2))
    print head.toList()
    head = s.oddEvenList(head)
    print head.toList()
    print "1->2 is expected"
