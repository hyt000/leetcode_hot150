class Solution:
    # 1. 前序遍历
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root,res)
        return res

    def dfs(self,node,res):
        if not node: return
        res.append(node.val) # 第一步：访问根节点
        self.dfs(node.left,res)       # 第二步：递归左子树
        self.dfs(node.right,res)      # 第三步：递归右子树