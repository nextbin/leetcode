#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: latios


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ret = ''
        for i in range(n):
            # 2k+1
            for j in range(n):
                if (i - j < 0) | (i + j >= n):
                    break
                if s[i - j] != s[i + j]:
                    break
                elif len(ret) < j * 2 + 1:
                    ret = s[i - j:i + j + 1]
            # 2k
            for j in range(n):
                if (i - j < 0) | (i + 1 + j >= n):
                    break
                if s[i - j] != s[i + 1 + j]:
                    break
                elif len(ret) < j * 2 + 2:
                    ret = s[i - j:i + 1 + j + 1]
        return ret
