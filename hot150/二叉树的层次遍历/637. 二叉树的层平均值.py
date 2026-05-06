# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        root_list = deque([root])
        next_root = []
        res = []
        c_sum = 0
        nums = 0
        while root_list:
            now_root = root_list.popleft()
            c_sum += now_root.val
            nums += 1
            if now_root.left:
                next_root.append(now_root.left)
            if now_root.right:
                next_root.append(now_root.right)
            if not root_list:
                res.append(c_sum/nums)
                c_sum = 0
                nums = 0
                root_list.extend(next_root)
                next_root = []
        return res

