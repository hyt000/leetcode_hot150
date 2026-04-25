# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

# 叶子节点 是指没有子节点的节点。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and  not root.left and not root.right:
            return True
        root.sum = root.val
        root_deque = deque([root])
        while root_deque:
            root_node = root_deque.popleft()
            if root_node.left:
                root_deque.append(root_node.left)
                root_node.left.sum = root_node.sum+root_node.left.val
                
            if root_node.right:
                root_deque.append(root_node.right)
                root_node.right.sum = root_node.sum+root_node.right.val
                
            if not root_node.left and not root_node.right:
                if root_node.sum == targetSum:
                    return True

        return False