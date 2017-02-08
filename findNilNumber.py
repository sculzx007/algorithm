#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys 
tmp = [1,3,2,7,4,6,0,10]
#getMinNil_A(tmp)

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
    print getMinNil_A(tmp)
    print getMinNil_B(tmp)
else :
    tmp = []
    for i in range(len(sys.argv)) :
        if i > 0 :
          #  print i-1,sys.argv[i]
            tmp.insert(i-1,int(sys.argv[i]))
    print getMinNil_A(tmp)
    print getMinNil_B(tmp)
