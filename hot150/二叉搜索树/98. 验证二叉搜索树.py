# Definition for a binary tree node.
from collections import deque
"""
想法一：层序遍历，这个结果不对。因为右子节点也要比根节点大
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        ans = []
        def inorder(node):
            nonlocal ans
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        temp = ans.copy()
        temp.sort()
        if temp==ans:
            if len(set(temp)) == len(ans):
                return True
            else:
                return False
        else:
            return False



