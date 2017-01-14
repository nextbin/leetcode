#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: latios

"""
Reference:
    https://discuss.leetcode.com/topic/8909/clear-python-code-straight-forward
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
        root = ListNode(0)
        curr = root
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            v = v1 + v2 + carry
            carry, v = divmod(v, 10)
            curr.next = ListNode(v)
            curr = curr.next
        return root.next
