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
            





            