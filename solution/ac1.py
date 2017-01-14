#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: latios

"""
Notes:
    len(object):
        return length of object
    range(stop):
        return list [0, 1, 2, 3, ..., stop-1]
    range(start,stop=None,step=None):
        return list [start, start+step, ..., start+step*k] where start+step*k < stop
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sz = len(nums)
        for i in range(sz):
            for j in range(i + 1, sz):
                if nums[i] + nums[j] == target:
                    return [i, j]


# solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))
