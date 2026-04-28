

# 二叉树中的最大路径和
# 题目编号：124
# binary-tree-maximum-path-sum


"""
1. 我要向子节点索取什么？（过滤负资产）
物理意义： 我需要左右子树提供一条连续路径。但如果他们给的是负数（只会拖累我），我直接当他们不存在（取 0）。
2. 我的对内任务是什么？（拼凑全局最大 V 型）
物理意义： 假设我就是这条路径的最高点，我把我能拿到的所有正收益（左 + 我自身 + 右）全加起来，
去全局记分板上碰碰运气，看能不能打破历史记录。
3. 我的对外任务是什么？（向上级汇报单边最大值）
物理意义： 我的父节点在等我（必须包含父节点），所以二叉树不能分叉，
我只能把我自己（node.val），加上左右两边中较大的一条边，捆绑成一条不分叉的线头，递给父节点。
"""







from typing import List
import math

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def binary_tree_maximum_path_sum(self, nums: List[int], target: int) -> List[int]:
        # --- 在这里编写代码 ---
        pass
# leetcode submit region end(Prohibit modification and deletion)

# 本地调试代码（可选）
if __name__ == "__main__":
    s = Solution()
    # 在这里写测试用例，例如：
    # result = s.twoSum([2,7,11,15], 9)
    # print(result)