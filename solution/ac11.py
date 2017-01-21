#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: latios

"""
https://discuss.leetcode.com/topic/14940/simple-and-clear-proof-explanation
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height) < 2:
            return 0
        ret = 0
        i = 0
        j = len(height) - 1
        while i < j:
            ret = max(ret, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return ret
