

# 完全二叉树的节点个数
# 题目编号：222
# count-complete-tree-nodes
"""
解题：
你站在根节点看左右子树，一定会出现一种情况：
左子树是满的
或者：
右子树是满的
也就是说，每次至少有一边可以直接用公式算，不需要递归数。
同时注意到，这个题由是可以不断拆成一个小树计算有多少个节点，于是用递归，
那么，
1.  递归的终止条件是什么？
    也就是这个函数处理到什么情况，答案已经简单到不需要继续拆了？
    不难发现是root is None
    此时return 0
2.  那怎么判断哪边是满的？如果考虑左边第一个和root.right然后一直去左边
    一共有两种情况
    left_h==right__h,说明左边满
    和
    left>right_h说明右边满
3.  那怎么计算高度h？
    当最左边的节点存在，这个高度就加一
4.  左子树高度是 left_h，节点数是：
    2 ** left_h - 1
    再加上根节点，就是：
    2 ** left_h
    然后再加上右边的总节点数就可以。所以代码是：
    return (1 << left_h) + self.countNodes(root.right)
    不难想到第二种是return (1 << right_h) + self.countNodes(root.left)

"""
from typing import List
import math

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def count_complete_tree_nodes(self, nums: List[int], target: int) -> List[int]:
        # --- 在这里编写代码 ---
        pass
# leetcode submit region end(Prohibit modification and deletion)

# 本地调试代码（可选）
if __name__ == "__main__":
    s = Solution()
    # 在这里写测试用例，例如：
    # result = s.twoSum([2,7,11,15], 9)
    # print(result)