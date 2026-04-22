"""
1. Problem Description
把链表按每 `k` 个节点分组进行翻转；如果最后剩余不足 `k` 个，就保持原样不动。

2. Solution Approach
核心是“分组 + 局部翻转 + 重新接回”：
- 用 `left_node/right_node` 找到一组完整的 `k` 个节点。
- 先把这一段临时截断，调用 `paixv` 做组内翻转。
- 翻转后把前后链路重新接好，再继续下一组。

3. Code Walkthrough
- `dummy` 和 `pre_node`：方便处理第一组翻转时头节点变化。
- `count % k` 控制 `right_node` 前进，定位组尾。
- `temp_node = right_node.next` 先保存下一组起点。
- `right_node.next = None` 把当前组断开，避免翻转时串到后面。
- `paixv` 内通过头插法不断把后续节点插到组前，实现逆序。
- 最后 `right_node.next = temp_node` 把剩余链表接回去。

4. Key Takeaways
- 这题本质是“链表分段操作”，关键在断开和接回。
- 时间复杂度 O(n)，空间复杂度 O(1)。
- 常见坑：不足 `k` 个时误翻转、翻转后尾节点连接错误。
- 链表分组题建议固定模板：找组边界 -> 断开 -> 翻转 -> 接回。
"""
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre_node = dummy
        left_node = head
        right_node = head
        count = 1

        if k==1:
            return dummy.next

        else:
            while True:
                if count%k !=0:
                    right_node = right_node.next
                    count+=1
                    if not right_node:
                        return dummy.next
                else:
                    count=1

                    temp_node = right_node.next
                    right_node.next = None
                    last_node = self.paixv(pre_node,left_node,right_node)
                    right_node = last_node
                    right_node.next = temp_node
                    pre_node = right_node
                    right_node = right_node.next
                    left_node = right_node


                    if not right_node:
                        return dummy.next

    def paixv(self, pre_node, left_node, right_node):
        while True:
            cur_node = pre_node.next
            if left_node.next!=right_node:

                pre_node.next = left_node.next
                left_node.next = pre_node.next.next
                pre_node.next.next = cur_node
            else:
                pre_node.next = left_node.next
                pre_node.next.next = cur_node
                left_node.next = None
                return left_node


if __name__ == '__main__':
    def build_list(arr):
        dummy = ListNode()
        cur = dummy
        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next


    # 构建 head = 1->2->3->4->5
    head = build_list([1, 2, 3, 4,5])

    s = Solution()
    s.reverseKGroup(head, 2)


