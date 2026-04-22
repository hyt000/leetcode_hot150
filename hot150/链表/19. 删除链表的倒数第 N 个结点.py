# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next :
            return None
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        slow = head
        fast = head
        count = 0
        while  fast.next:
            if count == n-1:
                pre=pre.next
                slow = slow.next
                fast = fast.next
            else:
                fast = fast.next
                count += 1

        pre.next = slow.next
        return dummy.next