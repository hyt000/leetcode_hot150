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