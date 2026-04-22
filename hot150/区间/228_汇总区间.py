# 给定一个  无重复元素 的 有序 整数数组 nums 。
#
# 区间 [a,b] 是从 a 到 b（包含）的所有整数的集合。
#
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个区间但不属于 nums 的数字 x 。
#
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
#
# "a->b" ，如果 a != b
# "a" ，如果 a == b
"""
1. Problem Description
给一个有序且无重复的数组，把连续数字压缩成区间字符串：
- 单个数写成 `"a"`
- 连续段写成 `"a->b"`

2. Solution Approach
线性扫描分段：
- 用 `temp` 维护当前连续段。
- 下一个数如果是 `temp` 末尾 +1，就继续扩展。
- 否则当前段结束，存入 `list_`，再开新段。
- 最后把每段转成题目要求格式。

3. Code Walkthrough
- 先处理空数组和单元素的边界。
- `for num in nums` 持续构建 `temp`。
- 断开时把 `temp` 放进 `list_`，重置为新起点。
- 末尾还要再 `append(temp)`，避免漏最后一段。
- 最终根据段长度决定输出 `"a"` 或 `"a->b"`。

4. Key Takeaways
- 这是典型“连续段压缩”问题。
- 时间复杂度 O(n)，空间复杂度 O(n)（输出）。
- 常见坑：忘记处理最后一段。
- 这个模式可迁移到日志压缩、区间统计等场景。
"""
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        list_=[]
        temp=[]
        result_list=[]
        for num in nums:
            if not temp:
                temp.append(num)
                continue
            if num==temp[-1]+1:
                temp.append(num)
                continue
            else:
                list_.append(temp)
                temp=[num]
        list_.append(temp)
        for element in list_:
            if len(element)==1:
                result_list.append(str(element[0]))
            else:
                result_list.append(f"{element[0]}->{element[-1]}")
        return result_list