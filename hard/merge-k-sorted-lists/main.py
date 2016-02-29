#-*- coding: utf-8 -*-
# description: 合并k个排过序的链表，并描述其时空复杂度
# 思路：这个题比2个的merge要复杂些，关键在于每次不能循环k次遍历链表的列表！
# 而应该使用最小堆（heap）来解决这个问题。
#
# Definition for singly-linked _list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def toList(self):
        curr = self
        _list = []
        while curr:
            _list.append(curr.val)
            curr = curr.next
        return _list

    @staticmethod
    def genLinkedList(source):
        l1 = None
        for i in source[::-1]:
            l1 = ListNode(i, l1)
        return l1

import heapq
class Solution(object):
    def mergeKLists(self, _lists):
        """
        :type _lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for _list in _lists:
            if _list:
                heapq.heappush(h, (_list.val, _list))
                _list = _list.next
        #print h
        if not h:
            return None
        val, head = heapq.heappop(h)
        if head.next:
            heapq.heappush(h, (head.next.val, head.next))
        curr = head
        while h:
            #print h
            val, node = heapq.heappop(h)
            #print val
            curr.next = node
            curr = curr.next
            if node.next:
                node = node.next
                heapq.heappush(h, (node.val, node))

        return head

import random
def randomGenSortedList(limit, _list_num, repeat_probability=0.0):
    i = 0
    _list = []
    for n in xrange(_list_num):
        _list.append([])
    while i < limit:
        num = random.randint(0, _list_num - 1)
        _list[num].append(i)
        if repeat_probability <= random.uniform(0, 1.0):
            i += 1
    return _list

def randomGenSortedLinkedList(limit, _list_num, repeat_probability=0.0):
    _lists = randomGenSortedList(limit, _list_num, repeat_probability)
    return [ListNode.genLinkedList(_list) for _list in _lists]

if "__main__" == __name__:
    s = Solution()

    #print randomGenSortedList(32, 5)
    #print randomGenSortedList(32, 5, 0.5)
    #print randomGenSortedLinkedList(32, 5, 0.5)

    ## 注意处理空LinkedList！！
    _lists = randomGenSortedList(0, 5)
    #_lists = randomGenSortedList(32, 5)
    #_lists = randomGenSortedList(32, 32)
    #_lists = randomGenSortedList(32, 5, 0.5)
    print _lists
    print reduce(lambda x, y: sorted(x+y), _lists)
    _list = s.mergeKLists([ListNode.genLinkedList(_list) for _list in _lists])
    print _list
    print _list.toList()
