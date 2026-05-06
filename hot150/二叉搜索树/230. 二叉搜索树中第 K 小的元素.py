# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        now_k = 0
        ans = None
        def inorder(node):
            nonlocal now_k,ans
            if node is None:
                return ans
            if ans is not None:
                return ans

            inorder(node.left)
            now_k += 1
            if now_k == k:
                ans = node.val
                return  ans
            inorder(node.right)
            return ans
        inorder(root)
        return ans


