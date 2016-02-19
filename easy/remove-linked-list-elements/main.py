# -*- coding: utf-8 -*-
# description: 删除节点，为了便于处理尾节点，用改curr.next来删下一节点，而非用替换val来删curr节点。
# 只是在一开始要对头部做很特殊的处理。
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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        while head and val == head.val:
            head = head.next
        if not head:
            return head
        curr = head
        while curr.next:
            if val == curr.next.val:
                curr.next = curr.next.next
                continue
            curr = curr.next
        return head


if "__main__" == __name__:
    s = Solution()

    head = ListNode(6, ListNode(6, ListNode(6, ListNode(1, ListNode(2, ListNode(3, ListNode(6, ListNode(6, ListNode(4, ListNode(5, ListNode(6)))))))))))
    print head.toList()
    head = s.removeElements(head, 6)
    print head.toList()
    print "1->2->3->4->5 is expected"

    head = None
    print head
    head = s.removeElements(head, 6)
    print head
    print "None is expected"

    head = ListNode(6, ListNode(6, ListNode(6)))
    print head.toList()
    head = s.removeElements(head, 6)
    print head
    print "None is expected"
