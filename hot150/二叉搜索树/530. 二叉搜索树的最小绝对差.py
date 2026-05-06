# Definition for a binary tree node.
from cmath import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
"""
先回顾一下二叉搜索树的性质：
    左子节点一定比根节点小，
    右子节点一定大
完美契合中序遍历，
那我们可以记录左节点和中节点的差值和中和右的差值
"""
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = inf
        prev = None
        def middle_traversal(node):
            nonlocal ans,prev
            if not node:
                return
            middle_traversal(node.left)
            if prev is not None:
                ans = min(ans,node.val - prev)
            prev = node.val
            middle_traversal(node.right)

        middle_traversal(root)
        return ans
root = TreeNode(100000)
root.left = TreeNode()
s=Solution()
print(s.getMinimumDifference(root))