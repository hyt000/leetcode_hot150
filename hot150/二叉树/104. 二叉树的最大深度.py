"""
1. Problem Description
这题要我们求一棵二叉树有多“高”。从根节点一路往下走，到最深叶子节点，最长这条路径上有多少个节点，就是最大深度。

2. Solution Approach
核心是递归（深度优先遍历）。
- 对每个节点，分别算左子树最大深度和右子树最大深度。
- 当前节点的深度 = max(左深度, 右深度) + 1。
- 空节点深度记为 0，作为递归终止条件。
文件里还给了自顶向下写法：用 `depth` 往下传，用 `ans` 记录全局最大值。

3. Code Walkthrough
- `if root is None: return 0`：空树直接返回 0。
- `lmax = self.maxDepth(root.left)`：递归求左子树。
- `rmax = self.maxDepth(root.right)`：递归求右子树。
- `return max(lmax, rmax) + 1`：把当前节点算进去。
第二个 `Solution` 版本里，`from_head_to_foot` 每到一层就 `depth += 1`，最后更新 `ans`。

4. Key Takeaways
- 容易漏掉空树判断。
- 时间复杂度 O(n)，每个节点访问一次。
- 空间复杂度 O(h)，h 是树高（递归栈）。
- “树高度/深度”问题，优先想到“左右子树答案 + 1”的递归模板。
"""
# 给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
# Definition for a binary tree node.
from typing import Optional
#solution1:自下而上要答案，分解问题

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        lmax = self.maxDepth(root.left)
        rmax = self.maxDepth(root.right)
        return max(lmax, rmax)+1
#solution2:自上而下传状态
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def from_head_to_foot(node, depth):
            if node is None:
                return

            nonlocal ans
            depth += 1
            from_head_to_foot(node.left, depth)
            from_head_to_foot(node.right, depth)
            ans = max(ans, depth)
            return

        from_head_to_foot(root, 0)
        return ans


