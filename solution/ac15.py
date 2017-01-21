#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: latios


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        ret = []
        zero = 0
        cnt_dict = {}
        for val in nums:
            if val == 0:
                zero += 1
            if val > 0:
                cnt_dict[val] = cnt_dict.get(val, 0) + 1
        if zero >= 3:
            ret.append([0, 0, 0])
        for i in range(n):
            if nums[i] >= 0:
                break
            for j in range(i + 1, n):
                val = nums[i] + nums[j]
                if val >= 0:
                    continue
                if 0 < nums[j] < -val:
                    continue
                cnt = cnt_dict.get(-val, 0)
                if (-val == nums[j] and cnt >= 2) or (-val != nums[j] and cnt > 0):
                    if [nums[i], nums[j], -val] not in ret:
                        ret.append([nums[i], nums[j], -val])
        return ret
