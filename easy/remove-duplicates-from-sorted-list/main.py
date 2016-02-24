#-*- coding: utf-8 -*-
# description: 删除排序后的重复节点。
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        curr = head
        while curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

if "__main__" == __name__:
    s = Solution()

    ## 注意处理空LinkedList！！
    head = ListNode.genLinkedList([])
    print head
    head = s.deleteDuplicates(head)
    print "None is expected"

    head = ListNode.genLinkedList([1, 2, 3, 4, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "1->2->3->4->5 is expected"

    # head
    head = ListNode.genLinkedList([1, 1, 1, 2, 3, 4, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "1->2->3->4->5 is expected"

    # tail
    head = ListNode.genLinkedList([1, 2, 2, 3, 4, 5, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "1->2->3->4->5 is expected"

    # middle with conjunct targets
    head = ListNode.genLinkedList([1, 2, 2, 3, 3, 4, 4, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "1->2->3->4->5 is expected"

    # all-in-one
    head = ListNode.genLinkedList([1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "1->2->3->4->5 is expected"
