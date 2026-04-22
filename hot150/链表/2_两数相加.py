"""
1. Problem Description
两个数字用“逆序链表”表示（个位在前），要返回它们相加后的结果链表，结果也要是逆序。

2. Solution Approach
按位相加 + 进位：
- 同时遍历两条链表，取当前位数字相加，再加上 `carry`。
- 当前位写入 `total % 10`，进位更新为 `total // 10`。
- 当两条链表都结束后，如果还有进位，继续补一个节点。

3. Code Walkthrough
- `dummy/res`：方便逐步构建答案链表。
- `while l1 or l2 or carry`：保证最后进位也能处理。
- `val1 = l1.val if l1 else 0`：长度不一致时缺位补 0。
- `res.next = ListNode(value)`：追加当前位结果。
- 最终返回 `dummy.next`。

4. Key Takeaways
- 这题和手算加法一模一样，重点就是进位处理。
- 时间复杂度 O(max(m,n))，空间复杂度 O(max(m,n))（输出链表不计则额外 O(1)）。
- 常见坑：忘记处理最后一位进位。
- “链表逐位运算”类题都可直接套这个框架。
"""
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