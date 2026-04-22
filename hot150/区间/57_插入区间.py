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


