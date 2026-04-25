# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
            
        res = []
        cur = 0
        
        # 步骤 1：通过前序遍历（根-左-右）收集所有节点
        def dfs(root):
            if not root:return
            res.append(root)  # 将节点依次加入列表
            dfs(root.left)
            dfs(root.right)
            return 
            
        dfs(root)
        length = len(res)
        
        # 步骤 2：遍历收集到的节点，修改左右指针将其串联为单链表
        for node in res:
            if cur != length-1:
                node.right = res[cur+1]  # right 指针指向前序遍历结果的下一个节点
            else:
                node.right = None        # 最后一个节点的 right 指针为空
            node.left = None             # 根据题意，所有节点的 left 指针始终为空
            cur += 1
            
        return root

if __name__ == "__main__":
    def print_flattened_tree(root):
        curr = root
        res = []
        while curr:
            res.append(str(curr.val))
            if curr.left:
                res.append("(Error: left child is not None)")
            curr = curr.right
        return " -> ".join(res)

    # 构造测试用例 1: [1,2,5,3,4,null,6]
    #      1
    #    /   \
    #   2     5
    #  / \     \
    # 3   4     6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(6)

    sol = Solution()
    sol.flatten(root1)
    print("Test 1 Flatten:", print_flattened_tree(root1)) # 预期: 1 -> 2 -> 3 -> 4 -> 5 -> 6

    # 构造测试用例 2: []
    root2 = None
    sol.flatten(root2)
    print("Test 2 Flatten:", print_flattened_tree(root2)) # 预期: ""

    # 构造测试用例 3: [0]
    root3 = TreeNode(0)
    sol.flatten(root3)
    print("Test 3 Flatten:", print_flattened_tree(root3)) # 预期: "0"