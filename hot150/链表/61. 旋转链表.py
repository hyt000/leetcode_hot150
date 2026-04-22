"""
1. Problem Description
把链表整体向右旋转 `k` 次。每旋转一次，就是把尾节点拿到最前面。

2. Solution Approach
核心思路是“先成环，再断开”：
- 先遍历求链表长度 `count`，拿到尾节点。
- 真正要转的步数是 `k % count`（转一整圈等于没转）。
- 尾节点指向头节点，形成环。
- 从原头走到第 `count - rotate` 个节点，把那里断开，后一个节点就是新头。

3. Code Walkthrough
- 前面几个 `if` 处理空链表、`k==0`、单节点等边界情况。
- `while cur_node.next` 统计长度并定位尾节点。
- `rotate = k % count` 去掉无效轮转。
- `tail_node.next = head_node` 临时闭环。
- 再走到断开点：`head = cur_node.next`，`cur_node.next = None`。

4. Key Takeaways
- 一定要先做 `k % n`，否则会做很多无用操作。
- 时间复杂度 O(n)，空间复杂度 O(1)。
- 链表“整体移动”类题目经常用“成环 + 找断点”模板。
- 边界要重点测：空链表、1 个节点、`k` 是 `n` 的倍数。
"""
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if k == 0  or head.next == None:
            return head

        cur_node = head
        head_node = head
        count = 1
        while cur_node.next:
            cur_node = cur_node.next
            count += 1
        tail_node = cur_node

        rotate = k % count
        if rotate == 0:
            return head

        if head.next.next == None and rotate==1:
            head.next.next = head
            head = head.next
            head.next.next =None
            return head

        tail_node.next = head_node
        num = 1
        cur_node = head_node
        while num!= count -rotate:
            num+=1
            cur_node = cur_node.next
        head = cur_node.next
        cur_node.next = None
        return head
if __name__ == '__main__':
    def create_node(arr):
        dummy = ListNode()
        cur = dummy
        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next
    def print_node(head_node):
        while head_node:
            print(head_node.val)
            head_node = head_node.next


    head_node = create_node([1,2,3,4,5])
    solution = Solution()
    head = solution.rotateRight(head_node, 1)
    print_node(head)


