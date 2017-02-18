#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def minSubstring(string,target) :
    keys  = set(target)
    dct   = dict()
    head  = -1
    tail  = 0
    cnt   = 0
    tcnt  = 0
    for key in keys :
        dct[key] = 0
    cnt = len(dct)

    for char in string :
        if tcnt < cnt :
            head = head + 1
        if char in keys :
            dct[char] = dct[char] + 1
            if dct[char] == 1 :
                tcnt = tcnt + 1
        if tcnt == cnt :
            while (string[tail] in keys and dct[string[tail]] > 1) or (string[tail] not in keys):
                if string[tail] in keys :
                    dct[string[tail]]  = dct[string[tail]] - 1
                tail = tail + 1
            ttail = tail
            thead = head
            while thead < len(string) - 1 :
                thead = thead + 1
                if string[ttail] in keys :
                    dct[string[ttail]] = dct[string[ttail]] - 1
                    if dct[string[ttail]] == 0 :
                        tcnt = tcnt - 1
                if string[thead] in keys :
                    dct[string[thead]] = dct[string[thead]] + 1
                    if dct[string[thead]] == 1 :
                        tcnt = tcnt + 1
                ttail = ttail + 1
                if tcnt == cnt :
                    while (string[ttail] not in keys or dct[string[ttail]] > 1) :
                        if string[ttail] in keys :
                            dct[string[ttail]] = dct[string[ttail]] - 1
                        ttail = ttail + 1
                        tail = ttail
                        head = thead
            print ("起始位置：",tail,"结束位置",head,string[tail:head + 1])
            return [tail,head]

if len(sys.argv) == 1 :
    target = "ad"
    string = "ssasdad"
else :               
    target = sys.argv[2]
    string = sys.argv[1]
minSubstring(string,target)
