# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        temp_root = []
        root_list = deque([root])
        res = [[root.val]]
        flag = -1
        while root_list:
            now_root = root_list.popleft()
            if now_root.left:
                temp_root.append(now_root.left)
            if now_root.right:
                temp_root.append(now_root.right)
            if not root_list:

                if not temp_root:
                    return res
                if flag ==1:
                    res.append([a.val for a in temp_root])
                    flag *= -1
                elif flag == -1:
                    temp_root.reverse()
                    res.append([a.val for a in temp_root])
                    flag *= -1
                    temp_root.reverse()
                root_list.extend(temp_root)
                temp_root = []
