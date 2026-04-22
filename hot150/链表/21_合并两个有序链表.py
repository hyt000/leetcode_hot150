#重做！！！！！！！！！！！！！！！！！！！！！！
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        dummy.next = res
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if list1.val<=list2.val:
                val = list1.val
                res.next = ListNode(val=val)
                list1 = list1.next
                
            else:
                val = list2.val
                res.next = ListNode(val=val)
                list2 = list2.next
            res = res.next
        if list1 :
            res.next = list1
        elif list2:
            res.next = list2
        return dummy.next


if __name__=='__main__':
    # l1 = [1,2,4]
    # l2 = [1,3,4]
    l1 = ListNode(1)
    l12 =ListNode(2)
    l13 =ListNode(4)
    l2 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l1.next=l12
    l12.next = l13
    l2.next = l22
    l22.next = l23
    S=Solution()
    S.mergeTwoLists(l1,l2)
            

