#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def findSingleNumber(nums) :
    ret = 0;
    for num in nums:
        ret = ret ^ num
    return ret

if len(sys.argv) == 1 :
    nums = [1,3,2,1,3]
else :
    nums = []
    for i in range(len(sys.argv)) :
        if i > 0 :
            nums.insert(i-1,int(sys.argv[i]))
print findSingleNumber(nums)
