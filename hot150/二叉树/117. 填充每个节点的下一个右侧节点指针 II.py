# 给定一个二叉树：

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。

# 初始状态下，所有 next 指针都被设置为 NULL 。

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        root_deque = [root]
        next_deque = []
        while root_deque:
            len = len(root_deque)
            for num,node in enumerate(root_deque):
                if num == len-1:
                    node.next = None
                else: 
                    node.next = root_deque[num+1]
                
                if node.left:
                    next_deque.append(node.left)
                if node.right:
                    next_deque.append(node.right)
            root_deque = next_deque.copy()
            next_deque = None
        
        return root
