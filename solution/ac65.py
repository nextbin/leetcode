#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: latios

"""
Notes:
    try-except-finally
        异常机制。通过 raise ValueError 可以抛出异常
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except (ValueError, TypeError):
            return False
        return True
