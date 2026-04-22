"""
1. Problem Description
只反转链表中从 `left` 到 `right` 这段区间，其他位置保持不变。

2. Solution Approach
思路是局部头插法：
- 先找到反转区间前一个节点 `pre`，区间起点 `left_node`，区间终点 `right_node`。
- 在区间内不断把 `left_node` 后面的节点摘出来，插到 `pre` 后面。
- 重复直到 `right_node` 被移动到区间头部。

3. Code Walkthrough
- 代码分两种情况：`left != 1` 和 `left == 1`。
- 当 `left == 1` 时，额外引入 `fake_node`，避免头节点变化不好处理。
- `while True` 里：
  - 若 `left_node.next == right_node`，做最后一次调整并结束。
  - 否则执行一次头插：`pre.next = left_node.next`，并重连后续指针。
- 最后返回新的头节点（可能变化）。

4. Key Takeaways
- 局部反转最关键是找到“反转前驱节点 `pre`”。
- 时间复杂度 O(n)，空间复杂度 O(1)。
- `left == 1` 是高频边界，建议统一用 `dummy/fake_node` 处理。
- 每次改指针前先画出 3~4 个关键节点关系，错误率会明显下降。
"""
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
# 请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        if left==right:
            return head
        if left !=1:
            left_index = left-1
            right_index = right-1
            pre_index = left_index-1
            count = 0
            now = head
            while now:
                if count==pre_index:
                    pre = now
                    left_node = now.next
                if count==right_index:
                    right_node = now
                now = now.next
                count += 1

            while True:
                if left_node.next == right_node:
                    left_node.next = right_node.next
                    right_node.next = pre.next
                    pre.next = right_node
                    break
                else:
                    cur_node = pre.next
                    pre.next = left_node.next
                    left_node.next = pre.next.next
                    pre.next.next = cur_node
            return head
        else:
            fake_node = ListNode(0)
            fake_node.next = head
            count = -1
            left_index = left - 1
            right_index = right - 1
            pre_index = left_index - 1
            now = fake_node
            while now:
                if count == pre_index:
                    pre = now
                    left_node = now.next
                if count == right_index:
                    right_node = now
                now = now.next
                count += 1

            while True:
                if left_node.next == right_node:
                    left_node.next = right_node.next
                    right_node.next = pre.next
                    pre.next = right_node
                    break
                else:
                    cur_node = pre.next
                    pre.next = left_node.next
                    left_node.next = pre.next.next
                    pre.next.next = cur_node


            return pre.next




if __name__=='__main__':
    def build_list(arr):
        dummy = ListNode()
        cur = dummy
        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next

# 构建 head = 1->2->3->4->5
    head = build_list([1,2,3,4])
    
    left = 1
    right = 4
    s = Solution()
    s.reverseBetween(head,left,right)
            





            