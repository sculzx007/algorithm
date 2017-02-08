#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys 

def getMinNil_A(nums):
    dct = []
    for i in range(max(nums)+1):
        dct.insert(i,-1)
    for n in nums:
        dct[n] = n
    for index in range(len(dct)):
        if dct[index] != index :
            return index
    return len(dct)

def getMinNil_B(nums):
    for n in range(len(nums)) :
        while nums[n] < n :
             num = nums [nums[n]]
             nums[nums[n]] = nums [n] 
             nums[n] = num
    for i in range(len(nums)) :
        if i != nums[i] :
            return i
    return len(nums)

if len(sys.argv) == 1 :
    nums = [1,3,2,7,4,6,0,10]
else :
    nums = []
    for i in range(len(sys.argv)) :
        if i > 0 :
            nums.insert(i-1,int(sys.argv[i]))
print getMinNil_A(nums)
print getMinNil_B(nums)
