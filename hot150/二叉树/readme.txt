1. 什么是前序遍历，中序遍历，后序遍历。怎么实现？

答：这三种遍历方式都是基于深度优先搜索（DFS）的思想，它们的区别主要在于“访问当前根节点”的时机不同。

1. 前序遍历 (Preorder Traversal)：
   - 顺序：根节点 -> 左子树 -> 右子树
   - 适用场景：需要先处理当前节点，再处理子节点的情况（例如复制一棵二叉树、序列化二叉树）。

2. 中序遍历 (Inorder Traversal)：
   - 顺序：左子树 -> 根节点 -> 右子树
   - 适用场景：对于二叉搜索树 (BST)，中序遍历能够得到一个递增的有序序列。

3. 后序遍历 (Postorder Traversal)：
   - 顺序：左子树 -> 右子树 -> 根节点
   - 适用场景：需要先获取子节点的结果，才能推导当前节点结果的情况（例如计算二叉树的最大深度、释放/删除二叉树节点）。

下面是这三种遍历方式的 Python 代码实现（使用最常见的递归解法）：

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1. 前序遍历
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node: return
            res.append(node.val) # 第一步：访问根节点
            dfs(node.left)       # 第二步：递归左子树
            dfs(node.right)      # 第三步：递归右子树
        dfs(root)
        return res

    # 2. 中序遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)       # 第一步：递归左子树
            res.append(node.val) # 第二步：访问根节点
            dfs(node.right)      # 第三步：递归右子树
        dfs(root)
        return res

    # 3. 后序遍历
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)       # 第一步：递归左子树
            dfs(node.right)      # 第二步：递归右子树
            res.append(node.val) # 第三步：访问根节点
        dfs(root)
        return res
```
2. 怎么实现层序遍历（Level Order Traversal）？

答：层序遍历是基于广度优先搜索（BFS）的思想。顾名思义，它会按照从上到下、从左到右的顺序，一层一层地访问二叉树的节点。

实现要点：
层序遍历通常使用 **队列 (Queue)** 来实现，利用队列“先进先出” (FIFO) 的特性。

Python 代码实现：
在 Python 中，推荐使用 `collections.deque` 作为双端队列，它的 `popleft()` 操作时间复杂度是 O(1)，比普通列表的 `pop(0)` 更高效。

```python
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []
        queue = deque([root])  # 初始化队列，将根节点加入
        
        while queue:
            level_size = len(queue)  # 当前层的节点数量
            current_level = []       # 用于存储当前层的所有节点值
            
            # 依次将当前层的所有节点出队，并将它们的子节点入队
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # 如果有左子节点，加入队列
                if node.left:
                    queue.append(node.left)
                # 如果有右子节点，加入队列
                if node.right:
                    queue.append(node.right)
                    
            # 将当前层的结果加入最终结果集中
            res.append(current_level)
            
        return res
```

适用场景：
- 按层级处理/打印二叉树数据
- 求二叉树的最小深度（寻找最短路径）
- 图的广度优先搜索（BFS）在树结构上的特例

---

3. 如何在控制台可视化（画出）一棵二叉树？

答：在本地调试二叉树题目时，如果只能看到离散的节点而无法看到整体结构，会非常痛苦。
我们可以通过一种**变种的“右-根-左”中序遍历**，在控制台中将二叉树横向打印出来。

Python 可视化函数实现：

```python
def print_tree(node, prefix="", is_left=None):
    """
    在控制台以树状结构打印二叉树 (横向展示，根节点在最左侧)
    """
    if not node:
        return
    
    # 1. 先遍历右子树
    if node.right:
        # 如果当前节点是根节点(is_left is None)，子节点的前缀不需要增加额外缩进
        # 如果当前节点是左子节点(is_left is True)，它的右子树需要打印 "│   " 保持连接线
        # 如果当前节点是右子节点(is_left is False)，它的右子树只需要空格 "    "
        new_prefix = prefix + ("" if is_left is None else ("│   " if is_left else "    "))
        print_tree(node.right, new_prefix, False)
        
    # 2. 打印当前节点
    if is_left is None:
        print(prefix + str(node.val))  # 根节点前面没有折线
    else:
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        
    # 3. 后遍历左子树
    if node.left:
        # 和右子树同理，调整左子树的缩进符号
        new_prefix = prefix + ("" if is_left is None else ("    " if is_left else "│   "))
        print_tree(node.left, new_prefix, True)

# ========== 测试用例 ==========
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    # 构造一棵测试树
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    print("打印出来的二叉树结构如下：")
    print_tree(root)
```

如果你运行上面的代码，控制台会输出如下漂亮的横向树形图：
```text
    ┌── 6
┌── 3
1
│   ┌── 5
└── 2
    └── 4
```
（注：如果你把头向左歪 90 度，或者把屏幕顺时针旋转 90 度，这就是一棵标准的二叉树结构了！）