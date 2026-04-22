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


