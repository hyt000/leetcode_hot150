"""
1. Problem Description
给你一个链表和一个值 `x`，要把链表分成两段：前面都是 `< x` 的节点，后面都是 `>= x` 的节点。
同时每一段内部的原始相对顺序不能乱。

2. Solution Approach
这份代码是“原链表上调整指针”的做法：
- 用多个指针跟踪“小值区尾部”和“大值区的边界”。
- 扫描过程中，遇到小值节点时，把它插到小值区末尾。
- 遇到大值节点时，更新大值区相关指针，继续向后走。
思路可行，但实现分支很多，细节较绕。

3. Code Walkthrough
- `dummy`：统一处理头节点可能变化的情况。
- `last_thin_node`：小于 `x` 分区当前尾节点。
- `last_fat_node/recent_fat_node`：用于维护大于等于 `x` 分区的位置。
- 代码按“头节点是否小于 x”分了两大分支，分别处理节点插入和链路重连。
- 最后返回 `dummy.next` 作为新头节点。

4. Key Takeaways
- 链表重排最容易错在“next 指针断链/成环”。
- 时间复杂度 O(n)，空间复杂度 O(1)（原地调整）。
- 更稳的写法通常是“两个虚拟头（small/big）最后拼接”，逻辑会更清晰。
- 做链表题时先画图，再写每一步指针变化，能少很多 bug。
"""
# 给你一个链表的头节点head和一个特定值x
# 请你对链表进行分隔，使得所有小于x的节点都出现在大于或等于x的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        if head.next == None:
            return head


        dummy = ListNode()
        dummy.next = head
        find_node = head.next
        last_thin_node = None
        last_fat_node = None
        recent_fat_node = None
        if head.val < x:
            last_thin_node = head
            while find_node:

                if find_node.val < x:
                    if last_fat_node:
                        last_thin_node.next =find_node
                        recent_fat_node.next = find_node.next
                        find_node = find_node.next
                        last_thin_node.next.next = last_fat_node
                        last_thin_node = last_thin_node.next
                    else:
                        last_thin_node = find_node
                        find_node = find_node.next
                else:
                    if not last_fat_node:
                        last_fat_node = find_node
                        recent_fat_node = find_node
                        find_node = find_node.next
                    else:
                        recent_fat_node = find_node
                        find_node = find_node.next

        #必有fat
        else:
            last_fat_node = head
            recent_fat_node =head
            while find_node:
               if find_node.val < x:
                   if not last_thin_node:
                       recent_fat_node.next = find_node.next
                       last_thin_node = find_node
                       find_node = find_node.next
                       dummy.next = last_thin_node
                       last_thin_node.next = last_fat_node
                   else:
                       last_thin_node.next = find_node
                       last_thin_node = find_node
                       recent_fat_node.next = find_node.next
                       find_node = find_node.next
                       last_thin_node.next = last_fat_node
               #出现fat
               else:

                       recent_fat_node = find_node
                       find_node = find_node.next

        return dummy.next

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
    head = create_node([1,4,3,2,5,2])
    sol = Solution()
    head = sol.partition(head, 3)
    print_node(head)