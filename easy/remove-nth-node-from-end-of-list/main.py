# -*- coding: utf-8 -*-
# description: 单链表删除倒数第N个节点。
# 首先，用双指针，来一趟解决这个问题。
# 然后，对节点操作，就考虑3种情况：
# 1. head
# 2. tail
# 3. 中间的节点
# 移除head必须使用一个特殊技巧：换val，然后改指向。因为我们拿到的入参，是copy不是ref。
# 既然已经决定用上面这个技巧，那么，中间节点 是可以统一用这个算法。
#
# 但是tail节点无法使用这个算法。对于tail节点，必须知道前一个节点，才能删除尾部。
# 最终的方案是：发现 n == len(list) 的时候，用移除首节点的模式。其他情况下，用删除下一节点来实现。
#
# 另外，当head链表只有一个节点的时候，没法移除。我们没法把head变成一个空ref。

# 注意：
# 重新阅读了题设后，我们发现 rtype: ListNode，注意3点：
# 1. 删除首节点的话，直接返回第二个节点即可。
# 2. 如果是最后一个节点，则直接返回None。
# 3*. 题设没有提：能不能修改原有的列表。这里，是采用的修改的方案。
#
# 另外，
# 一般前一个节点用 previous 而不是 before。
# 双指针算法中，一般用 fast 和 slow，来指代2个指针。
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        before = head
        tail = head
        while tail.next:
            count += 1
            if n < count:
                before = before.next
            tail = tail.next
        if n > count:
            # remove head
            #head.val = head.next.val
            #head.next = head.next.next
            return head.next
        else:
            # remove before's next
            before.next = before.next.next
            return head

if "__main__" == __name__:
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print head.toList()

    head = s.removeNthFromEnd(head, 2)
    print head.toList()
    print "1->2->3->5 is expected"

    head = s.removeNthFromEnd(head, 4)
    print head.toList()
    print "2->3->5 is expected"

    head = s.removeNthFromEnd(head, 3)
    print head.toList()
    print "3->5 is expected"

    head = s.removeNthFromEnd(head, 1)
    print head.toList()
    print "3 is expected"

    head = s.removeNthFromEnd(head, 1)
    print head
    print "None is expected"
