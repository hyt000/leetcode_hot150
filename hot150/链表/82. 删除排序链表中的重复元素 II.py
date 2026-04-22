"""
1. Problem Description
在一个“已排序”链表里，把所有出现重复的值全部删掉，只保留“只出现一次”的节点。
比如 `1->2->3->3->4->4->5` 要变成 `1->2->5`。

2. Solution Approach
这份代码用双指针 + 标记位：
- `slow/fast` 用来观察当前值是否重复。
- `flag` 记录当前这段值是否出现过重复。
- `pre` 指向结果链表的最后一个“确定保留”的节点，方便跳过重复段。

3. Code Walkthrough
- `dummy.next = head`：防止头节点被删除时不好处理。
- 当 `slow.val == fast.val`：说明进入重复段，`flag=True`，继续推进 `fast`。
- 当值不等时：
  - 如果 `flag=True`，说明前一段是重复值，`pre.next = fast` 直接跳过。
  - 如果 `flag=False`，说明 `slow` 是唯一值，三指针一起前进。
- 处理到尾部时再根据 `flag` 做一次收尾。

4. Key Takeaways
- 排序链表的好处是：重复值一定连续出现。
- 时间复杂度 O(n)，空间复杂度 O(1)。
- 容易错在“重复段刚好在尾部”的处理。
- 涉及删除头节点时，`dummy` 基本是必备工具。
"""
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


