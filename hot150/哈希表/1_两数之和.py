# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
#
# 你可以按任意顺序返回答案。
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_tuple = {}
        dict_num={}
        for index,num in enumerate(nums):
            if num not in dict_num or target==2*num:
                dict_num[num]=index
            else:
                continue

            cha = target - num
            if cha>num:
                key = (num,cha)
            else:
                key = (cha,num)
            if not key in dict_tuple:
                dict_tuple[key] = [index]
            else:
                dict_tuple[key].append(index)
            if len(dict_tuple[key])==2:
                return [dict_tuple[key][0],dict_tuple[key][1]]
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))