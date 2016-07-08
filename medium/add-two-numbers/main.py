#-*- coding: utf-8 -*-
# description: 删除排序后的重复节点（II型），可能存在头和尾的删除，所以要复杂很多。
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

    @staticmethod
    def genLinkedList(source):
        head = None
        for i in source[::-1]:
            head = ListNode(i, head)
        return head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        previous = ListNode(None)
        cur = previous
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return previous.next

if "__main__" == __name__:
    s = Solution()

    l1 = ListNode.genLinkedList([1, 2, 3, 4, 5])
    l2 = ListNode.genLinkedList([1, 2, 3, 4, 5])
    print l1.toList()
    print l2.toList()
    head = s.addTwoNumbers(l1, l2)
    print head.toList()
    print "2->4->6->8->0->1 is expected"

    l1 = ListNode.genLinkedList([2, 4, 3])
    l2 = ListNode.genLinkedList([5, 6, 4])
    print l1.toList()
    print l2.toList()
    head = s.addTwoNumbers(l1, l2)
    print head.toList()
    print "7->0->8 is expected"

    l1 = ListNode.genLinkedList([9, 9, 9])
    l2 = ListNode.genLinkedList([1, 2, 3, 4, 5])
    print l1.toList()
    print l2.toList()
    head = s.addTwoNumbers(l1, l2)
    print head.toList()
    print "0->2->3->5->5 is expected"
