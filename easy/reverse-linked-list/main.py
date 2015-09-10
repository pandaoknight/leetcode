# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        b = head
        head = head.next
        b.next = None
        while head:
            n = head.next
            head.next = b
            b = head
            head = n
        return b
