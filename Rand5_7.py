#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import time

def Rand5() :
    return random.randint(1,5)

def Rand7() :
    rnd = 5*(Rand5() - 1) + Rand5()
    if rnd >21 :
        return Rand7()
    else :
        return rnd % 7 + 1

def Rand7s() :
    lst = [[1,2,3,4,5],[6,7,1,2,3,],[4,5,6,7,1],[2,3,4,5,6],[7,0,0,0,0]]
    x = Rand5() - 1
    y = Rand5() - 1
    if lst[x][y] == 0 :
        return Rand7s()
    else :
        return lst[x][y]

if __name__ == "__main__" :
    dct1 = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    dct2 = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}
    cnt1 = 0
    cnt2 = 0
    tm = time.time()
    while cnt1<1000000 :
        nmb = Rand7()
        dct1[nmb] = dct1[nmb] + 1
        cnt1 = cnt1 + 1 
    print time.time() - tm
    tm = time.time()
    while cnt2<1000000 :
        nmb = Rand7s()
        dct2[nmb] = dct2[nmb] + 1
        cnt2 = cnt2 + 1
    print time.time() - tm

    print dct1
    print dct2
