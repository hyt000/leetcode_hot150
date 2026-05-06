# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
'''
层次遍历
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def layer_traversal(node):

            new_root = []
            res = []
            root_list = deque([node])
            while root_list:
                now_root = root_list.popleft()

                if now_root.left:
                    new_root.append(now_root.left)
                if now_root.right:
                    new_root.append(now_root.right)

                if not root_list:
                    res.append(now_root.val)
                    root_list.extend(new_root)
                    new_root = []
            return res
        res = layer_traversal(root)
        return res

if __name__ == "__main__":
        s = Solution()
        res = s.rightSideView(None)


