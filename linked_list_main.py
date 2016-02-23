# -*- coding: utf-8 -*-
# description: 通用链表模板
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
    pass

if "__main__" == __name__:
    s = Solution()

    ## 注意处理空LinkedList！！
    head = ListNode.genLinkedList([])
    print head
    #head = s.
    print "None is expected"

    head = ListNode.genLinkedList([1, 2, 3, 4, 5])
    print head.toList()
    #head = s.
    print head.toList()
    print "1->2->3->4->5 is expected"
