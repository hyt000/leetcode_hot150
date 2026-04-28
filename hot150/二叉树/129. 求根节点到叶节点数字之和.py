# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：
from typing import Optional

from collections import deque


# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。

# 叶节点 是指没有子节点的节点。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        root.sum = root.val

        def dfs(root:TreeNode):
            root_list = deque([root])
            cur_level = []
            res = []
            while root_list:
                length = len(root_list)

                for _ in range(length):
                    now_root = root_list.popleft()
                    if now_root.left:
                        now_root.left.sum = now_root.sum*10+now_root.left.val
                        root_list.append(now_root.left)
                    if now_root.right:
                        now_root.right.sum = now_root.sum*10 + now_root.right.val
                        root_list.append(now_root.right)
                    if not now_root.left and not now_root.right:
                        res.append(now_root.sum)
            return res
        res = dfs(root)
        result = sum(res)
        return result








if __name__ == '__main__':
    # 测试用例 1: 
    #   1
    #  / \
    # 2   3
    # 预期: 12 + 13 = 25
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    
    sol = Solution()
    print("测试用例 1 输出:", sol.sumNumbers(root1), " 预期: 25")

    # 测试用例 2:
    #     4
    #    / \
    #   9   0
    #  / \
    # 5   1
    # 预期: 495 + 491 + 40 = 1026
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    
    print("测试用例 2 输出:", sol.sumNumbers(root2), " 预期: 1026")
