# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder:
#             return None
#         root_val = preorder[0]
#         root = TreeNode(root_val)
#         # 这里是先序遍历的第一个元素，也是中序遍历的根节点
#         mid = inorder.index(preorder[0])
#         left_inorder = inorder[:mid]
#         right_inorder = inorder[mid+1:]
#         left_size = len(left_inorder)
#         left_preorder = preorder[1:left_size+1]
#         right_preorder = preorder[left_size+1:]
#         root.left = self.buildTree(left_preorder, left_inorder)
#         root.right = self.buildTree(right_preorder, right_inorder)
#         return root



# 接下来我要自己独立实现
class Solution:
    """
    解题思路提示：
    1. 前序遍历的特点：[根节点, [左子树的前序遍历结果], [右子树的前序遍历结果]]。
       因此，preorder 的第一个元素（preorder[0]）永远是当前子树的根节点。
    2. 中序遍历的特点：[[左子树的中序遍历结果], 根节点, [右子树的中序遍历结果]]。
    3. 我们可以在 inorder 中找到根节点的位置，从而确定左子树和右子树的节点数量。
    4. 知道了左子树的节点数量后，就可以在 preorder 中划分出左子树和右子树的前序遍历部分。
    5. 最后，递归地根据左右子树的前序、中序序列来构造左右子树。
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 递归终止条件：如果前序遍历数组为空，说明没有节点了，返回 None
        if not preorder:
            return None
        
        # 1. 确定根节点：前序遍历的第一个元素就是当前的根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. 在中序遍历中找到根节点的位置索引
        inorder_root_locate = inorder.index(root_val)
        
        # 3. 切割中序遍历数组：
        # 根节点左边的是左子树的中序遍历结果，右边的是右子树的中序遍历结果
        inorder_left_son_tree = inorder[:inorder_root_locate]
        inorder_right_son_tree = inorder[inorder_root_locate+1:]
        
        # 4. 获取左子树的节点数量，以此来切割前序遍历数组
        len_left_son_tree = len(inorder_left_son_tree)
        # len_right_son_tree = len(inorder_right_son_tree) # 其实这里不需要特意计算右子树长度
        
        # 5. 切割前序遍历数组：
        # 第一个元素 (索引 0) 是根节点，跳过；
        # 紧接着的 len_left_son_tree 个元素是左子树的前序遍历结果；
        # 剩下的全是右子树的前序遍历结果
        preorder_left_son_tree = preorder[1:len_left_son_tree+1]
        preorder_right_son_tree = preorder[len_left_son_tree+1:]
        
        # 6. 递归构造左子树和右子树
        root.left = self.buildTree(preorder_left_son_tree, inorder_left_son_tree)
        root.right = self.buildTree(preorder_right_son_tree, inorder_right_son_tree)
        
        return root





if __name__ == "__main__":
    print("test")
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    s = Solution()
    root = s.buildTree(preorder, inorder)
    print(root.val)

