# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，
# 满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false

"""
1. Problem Description
判断数组里是否存在两个相同数字，它们的下标距离不超过 `k`。

2. Solution Approach
哈希表记录“最近一次出现的位置”：
- 扫描数组。
- 如果当前数字之前出现过，就算一下下标差。
- 差值 `<= k` 立刻返回 `True`。
- 否则更新这个数字的最新下标，继续扫。

3. Code Walkthrough
- `dict_num[num] = index` 保存每个数字最近位置。
- 命中重复时用 `abs(dict_num[num]-index)` 判断距离。
- 不满足条件就覆盖旧下标，保证后续比较的是“最近一次”。
- 扫完都没命中返回 `False`。

4. Key Takeaways
- “最近位置”是这题最关键的信息。
- 时间复杂度 O(n)，空间复杂度 O(n)。
- 常见坑：不更新下标会错过更近的一对重复元素。
- 这类“值到位置映射”问题优先考虑哈希表。
"""
from typing import List
# num in dict（键存在性判断）和 dict.get(num)时间复杂度均为 O (1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_num={}
        for index,num in enumerate(nums):
            if num in dict_num:
                if abs(dict_num[num]-index)<=k:
                    return True
                else:
                    dict_num[num]=index
            else:
                    dict_num[num]=index

        return False

if __name__ == '__main__':
    nums = [1, 2, 3, 1,2,3]
    k = 2
    a = Solution()
    ans = a.containsNearbyDuplicate(nums, k)
    print(ans)


