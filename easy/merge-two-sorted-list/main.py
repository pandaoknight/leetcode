#-*- coding: utf-8 -*-
# description: 合并两个排过序的链表，要求不能重新生成一个崭新的列表
# 这下不能直接使用Python的list.sort()了
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
        l1 = None
        for i in source[::-1]:
            l1 = ListNode(i, l1)
        return l1

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if not l1:
            curr.next = l2
        else:
            curr.next = l1
        return head

if "__main__" == __name__:
    s = Solution()

    ## 注意处理空LinkedList！！
    l1 = ListNode.genLinkedList([])
    l2 = ListNode.genLinkedList([])
    print l1
    print l2
    print s.mergeTwoLists(l1, l2)
    print "None is expected"

    l1 = ListNode.genLinkedList([1])
    l2 = ListNode.genLinkedList([])
    print l1.toList()
    print l2
    print s.mergeTwoLists(l1, l2).toList()
    print "1 is expected"

    # begin with l1
    l1 = ListNode.genLinkedList([1, 2])
    l2 = ListNode.genLinkedList([2])
    print l1.toList()
    print l2.toList()
    print s.mergeTwoLists(l1, l2).toList()
    print "1 2 2 is expected"

    # begin with l2
    l1 = ListNode.genLinkedList([2, 3, 4, 5, 6])
    l2 = ListNode.genLinkedList([2, 7, 8, 9, 10])
    print l1.toList()
    print l2.toList()
    print s.mergeTwoLists(l1, l2).toList()
    print "2 2 3 4 5 6 7 8 9 10 is expected"

