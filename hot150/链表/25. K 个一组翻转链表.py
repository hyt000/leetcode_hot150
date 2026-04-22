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


