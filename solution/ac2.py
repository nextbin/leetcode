#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: latios

"""
Notes:
    `object` is not None:
        检查object是否为空
    while `boolean expression`:
        循环体while
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = []
        jin = 0
        while l1 is not None:
            val = l1.val + l2.val + jin
            jin = 0
            if val > 9:
                jin = 1
                val -= 10
            ret.append(val)
            l1 = l1.next
            l2 = l2.next
            if l2 is None and l1 is not None:
                l2 = ListNode(0)
        while l2 is not None:
            val = l2.val + jin
            jin = 0
            if val > 9:
                jin = 1
                val -= 10
            ret.append(val)
            l2 = l2.next
        if jin == 1:
            ret.append(1)
        return ret


solution = Solution()
a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3
print(solution.addTwoNumbers(a1, b1))

a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3
print(solution.addTwoNumbers(a2, b1))

a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3
print(solution.addTwoNumbers(a1, b2))
