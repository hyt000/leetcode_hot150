"""
1. Problem Description
删除链表的倒数第 `n` 个节点，并返回新的头节点。

2. Solution Approach
核心是快慢指针：
- 让 `fast` 先走 `n` 步，和 `slow` 拉开距离。
- 然后 `fast/slow` 一起走，直到 `fast` 到尾部。
- 这时 `slow` 正好在要删节点，`pre` 在它前面，执行删除即可。

3. Code Walkthrough
- `dummy.next = head`：统一处理删除头节点。
- `pre` 指向 `slow` 前一个节点。
- `while fast.next` 循环里，先让 `fast` 走；当计数达到 `n-1` 后，再同步推进 `pre/slow`。
- 循环结束后 `pre.next = slow.next`，把目标节点跳过去。

4. Key Takeaways
- 双指针“固定间距”是倒数第 K 类题的经典套路。
- 时间复杂度 O(n)，空间复杂度 O(1)。
- 要特别处理单节点链表、删除头节点等边界。
- 写链表删除时，先想清楚“谁指向谁”，再动 `next`。
"""
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