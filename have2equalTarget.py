#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def have2children(target,arr) :
    bowl = set(arr)
    for i in arr :
        if target - i in bowl :
            print(target-i,i)

def have2children_2(target,arr) :
    bowl = dict()
    for i in arr :
        if i in bowl :
            bowl[i] = bowl[i] + 1
        else :
            bowl[i] = 1
    for i in arr :
        if target - i in bowl :
            if target != 2*i or (bowl[target - i] >1) :
                print (target -i , i)

if len(sys.argv) == 1 :
    target = 11
    nums   = [1,3,2,7,4,6,0,10]
else :
    nums = []
    for i in range(len(sys.argv)) :
        if i == 1 :
            target = int(sys.argv[i])
        if i > 1 :
            nums.insert(i-1,int(sys.argv[i]))
print("使用不可包含二值相同的方案：")
have2children(target,nums)
print("兼容两值相同的方案：")
have2children_2(target,nums)
