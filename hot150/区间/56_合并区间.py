# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间
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




