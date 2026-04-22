# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if head.next is None:
            return head

        dummy = ListNode()
        dummy.next = head
        pre=dummy
        slow = head
        fast = head.next
        flag=False
        while True:
            if slow.val == fast.val:
                flag=True
                if fast.next:
                    fast = fast.next
                else:
                    pre.next =None
                    return dummy.next
            else:
                if fast.next:
                    if flag:
                        pre.next = fast
                        slow = fast
                        fast = fast.next

                        flag = False
                    else:
                        pre = pre.next
                        slow = slow.next
                        fast = fast.next

                else:
                    if flag:
                        pre.next = fast
                        slow = fast

                        flag = False

                    return dummy.next


