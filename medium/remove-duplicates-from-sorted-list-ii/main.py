#-*- coding: utf-8 -*-
# description: 删除排序后的重复节点（II型），可能存在头和尾的删除，所以要复杂很多。
# 先做头处理，这样保证第一个节点是不被删除的，然后再用"val型"删除。
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
        while True:
            if not head or not head.next:
                return head
            if head.next.val == head.val:
                temp = head
                while temp and temp.val == head.val:
                    temp = temp.next
                head = temp
            else:
                break

        if not head:
            return head
        curr = head
        while curr.next:
            next_val = curr.next.val
            if curr.next.next and next_val == curr.next.next.val:
                fast = curr.next
                while fast and next_val == fast.val:
                    fast = fast.next
                curr.next = fast
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
    print "2->3->4->5 is expected"

    # head to None
    head = ListNode.genLinkedList([1, 1])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head
    print "None is expected"

    # head with conjunction
    head = ListNode.genLinkedList([1, 1, 1, 2, 2, 3, 3, 4, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "4->5 is expected"

    # tail
    head = ListNode.genLinkedList([1, 2, 2, 3, 4, 5, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "1->3->4 is expected"

    # middle with conjunct targets
    head = ListNode.genLinkedList([1, 2, 2, 3, 3, 4, 4, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "1->5 is expected"

    # middle with conjunct targets and conjunct head
    head = ListNode.genLinkedList([1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head.toList()
    print "3 is expected"

    # all-in-one
    head = ListNode.genLinkedList([1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5])
    print head.toList()
    head = s.deleteDuplicates(head)
    print head
    print "None is expected"
