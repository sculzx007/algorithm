#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        rt  = ListNode(0)
        rrt = rt
        while l1.next != None and l2.next != None:
            rt.next = ListNode((l1.val + l2.val + rt.val) / 10)
            rt.val = (l1.val + l2.val + rt.val) % 10
            l1 = l1.next
            l2 = l2.next
            rt = rt.next
        while l1.next != None:
             if l2 == None:
                 tmp = 0
             else :
                 tmp = l2.val
                 l2 = l2.next
             rt.next = ListNode((l1.val + rt.val + tmp ) / 10)
             rt.val = (l1.val + rt.val + tmp) % 10
             l1 = l1.next
             rt = rt.next
        while l2 != None and l2.next != None:
             if l1 == None:
                 tmp = 0
             else :
                 tmp = l1.val
                 l1 = l1.next
             rt.next = ListNode((l2.val + rt.val + tmp) / 10)
             rt.val = (l2.val + rt.val + tmp) % 10
             l2 = l2.next
             rt = rt.next
        if l2 != None and l2.val != 0:
            if rt.val + l2.val > 9:
                rt.next =  ListNode((l2.val + rt.val) / 10)
            rt.val = (rt.val + l2.val) % 10
        if l1 !=None and l1.val != 0:
            if rt.val + l1.val > 9:
                rt.next =  ListNode((l1.val + rt.val) / 10)
            rt.val = (rt.val + l1.val) % 10
        return rrt
            
             
        
        