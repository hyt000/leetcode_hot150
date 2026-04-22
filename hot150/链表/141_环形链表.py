"""
1. Problem Description
判断单链表里有没有环：也就是沿着 `next` 一直走，会不会回到之前访问过的节点。

2. Solution Approach
代码使用快慢指针思想：
- 慢指针每次走一步，快指针每次走两步。
- 如果有环，快慢指针最终一定会相遇。
- 如果无环，快指针会先走到空。

3. Code Walkthrough
- 初始化 `fast = head.next.next`、`slow = head.next`，让两者速度不同。
- 循环中比较二者地址（`id`）是否相同，相同则返回 `True`。
- 若快指针无法继续前进，说明无环，返回 `False`。

4. Key Takeaways
- 判环最经典就是快慢指针（Floyd 判圈）。
- 理论复杂度 O(n) 时间、O(1) 额外空间。
- 实现时要先做空节点与短链表保护，否则容易空指针异常。
- 判断“是不是同一节点”本质比的是节点对象，而不是节点值。
"""
'''
重做！
'''
# 给你一个链表的头节点 head ，判断链表中是否有环。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 运行代码后发现所有节点 val 都是 1，但地址却不一样，对此产生疑问
# 地址不同的原因：
# 每个ListNode(1)都会创建一个独立的对象，val=1只是对象的属性值，属性值相同不代表对象相同；
# 内存地址标识的是 “对象本身”，而非对象的属性值，因此即使 4 个节点的val都是 1，它们仍是 4 个不同的对象，地址必然不同；
# 只有多个变量指向同一个对象（别名）时，地址才会相同。

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not  head.val:
            return False
        fast = head.next.next
        slow = head.next

        while id(fast):
             if id(fast)==id(slow):
                 return True
             fast = fast.next.next
             slow = slow.next
        return False
