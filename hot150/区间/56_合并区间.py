# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间
"""
1. Problem Description
给一堆区间，可能有重叠。要求把所有重叠部分合并，最后返回互不重叠的区间列表。

2. Solution Approach
标准“排序 + 扫描”：
- 按区间起点升序排序。
- 维护一个当前合并区间 `list_nums`。
- 新区间若与当前重叠，就扩展右边界。
- 不重叠就把当前区间加入结果，并开始新的当前区间。

3. Code Walkthrough
- `sorted_list = sorted(intervals, key=lambda x: x[0])`。
- `if l[0] <= list_nums[-1]` 判定重叠。
- 若重叠且右端更大，更新当前区间右端。
- 否则把当前区间 `append` 到 `res`，切换到新区间。
- 循环结束别忘再把最后一个当前区间放入结果。

4. Key Takeaways
- 区间合并是非常高频模板题。
- 时间复杂度 O(n log n)，空间复杂度 O(n)（结果集）。
- 容易漏掉最后一段区间的入结果操作。
- “先排序，再一遍扫”是区间题的核心套路。
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        list_nums = []
        res=[]
        sorted_list = sorted(intervals, key=lambda x: x[0])
        for l  in sorted_list:
            if not list_nums:
                list_nums.extend(l)
                continue
            if l[0]<=list_nums[-1]:
                if l[1]<=list_nums[-1]:
                    continue
                else:
                    list_nums.pop(-1)
                    list_nums.append(l[-1])
            else:
                res.append(list_nums)
                list_nums = l
        res.append(list_nums)
        return res

if __name__ == '__main__':
    nums = [[1, 3], [2, 6], [8, 10], [15, 18]]
    solution = Solution()
    print(solution.merge(nums))




