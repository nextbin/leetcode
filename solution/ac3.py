#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: latios

"""
Notes:
    dict = {}
        字典结构
        dict.get(object)
            返回object对应的值或None
        dict[key]=value
            对字典赋key-value值
    max(a,b)
        返回较大值
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        maxMap = {}
        ret = 0
        bg = 0
        for i in range(len(s)):
            ma = maxMap.get(s[i])
            if ma is None:
                ret = max(ret, i + 1 - bg)
            else:
                tmp = i + 1 - max(bg, ma + 1)
                ret = max(ret, tmp)
                bg = max(bg, ma + 1)
            maxMap[s[i]] = i
        return ret
