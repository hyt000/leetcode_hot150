# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 递归终止条件：如果后序遍历数组为空，说明没有节点了，返回 None
        if not postorder:
            return None
        # 先找到根节点，在后序遍历中是最后一个
        root_val = postorder[-1]
        root = TreeNode(root_val)
        # 找到中序遍历的根节点位置
        inorder_root_locate = inorder.index(root_val)
        # 分割 inorder 和 postorder,分成左子节点和右子节点
        inorder_left_son_tree = inorder[:inorder_root_locate]
        inorder_right_son_tree = inorder[inorder_root_locate+1:]
        postorder_left_son_tree = postorder[:len(inorder_left_son_tree)]
        postorder_right_son_tree = postorder[len(inorder_left_son_tree):-1]
        root.left = self.buildTree(inorder_left_son_tree, postorder_left_son_tree)
        root.right = self.buildTree(inorder_right_son_tree, postorder_right_son_tree)
        return root
    
