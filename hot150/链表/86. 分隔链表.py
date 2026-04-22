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