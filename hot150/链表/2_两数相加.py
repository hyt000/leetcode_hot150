# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，
# 并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        dummy.next = res
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1+val2+carry
            value = total%10
            carry = total//10
            print(value)
            res.next = ListNode(value)
            res = res.next
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        return dummy.next

            
if __name__=='__main__':
    l1 = ListNode(2)
    l11 = ListNode(4)
    l12 = ListNode(3)
    l2 = ListNode(5)
    l21 = ListNode(6)
    l22 = ListNode(4)
    l1.next = l11
    l11.next = l12
    l2.next = l21
    l21.next =l22
    a = Solution()
    a.addTwoNumbers(l1=l1,l2=l2)




#     l1 =
# [9,9,9,9,9,9,9]
# l2 =
# [9,9,9,9]