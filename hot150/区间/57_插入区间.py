# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi]
# 表示第 i 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。
#
# 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。
#
# 返回插入之后的 intervals。
#
# 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。.



'''
切片赋值时右边必须是iterable
'''
"""
1. Problem Description
给定一个已经按起点排序且互不重叠的区间列表，再给一个新区间。要把新区间插进去，并在必要时和重叠区间合并。

2. Solution Approach
这份代码做法是：
- 先把新区域追加到原列表。
- 重新按起点排序。
- 线性扫描找出需要合并的连续区间范围。
- 用切片把这段替换成一个合并后的新区间。

3. Code Walkthrough
- `intervals.append(newInterval)` 后调用 `paixv` 排序。
- 扫描时用 `current` 维护当前合并段的右端点。
- `merge_list` 记录被并入的区间下标范围。
- 扫描结束后，用切片赋值把 `[new_begin:new_end]` 替换成一个新区间。

4. Key Takeaways
- 插入区间题本质还是“区间合并”的变体。
- 时间复杂度 O(n log n)（因为这版做了排序），空间复杂度 O(1)~O(n)。
- 常见坑：新区间在最前、最后，或被完全包含。
- 若利用原数组已排序且不重叠特性，可进一步做到线性合并 O(n)。
"""
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        begin, end = newInterval[0], newInterval[1]
        loc = []
        length = len(intervals)
        if not intervals:
            return [[begin, end]]
        if not newInterval:
            return intervals
        intervals.append(newInterval)
        intervals = self.paixv(intervals)
        current = None
        merge_list = []
        for index,interval in enumerate(intervals):
            if  current is None:
                current = interval[-1]
                merge_list.append(index)
                continue
            if current>=interval[0]:
                merge_list.append(index)
                if current<interval[1]:
                    current = interval[1]
                else:
                    continue

            else:
                if len(merge_list)>=2:
                    break
                merge_list = [index]
                current = interval[-1]
        new_begin = merge_list[0]
        new_end = merge_list[-1]
        if new_end==length:
            intervals[new_begin:]=[[intervals[new_begin][0],current]]
            return intervals
        else:
            intervals[new_begin:new_end+1]=[[intervals[new_begin][0],current]]

            return intervals



    def paixv(self, nums):
        nums.sort(key=lambda x: x[0])
        return nums



if __name__ == '__main__':
    # intervals =[[1, 5]]
    # newInterval =[0, 6]
    # 预期结果
    # [[0, 5]]

    intervals =[[0,5],[8,9]]
    newInterval =[3,4]

    print(Solution().insert(intervals, newInterval))


