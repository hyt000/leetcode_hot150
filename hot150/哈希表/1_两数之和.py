# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
#
# 你可以按任意顺序返回答案。
"""
1. Problem Description
在数组中找两个数，它们的和等于 `target`，返回这两个数的下标。

2. Solution Approach
这份代码用哈希结构记录组合信息：
- 遍历每个数 `num`，计算它需要的配对值 `cha = target - num`。
- 把同一对可能组合收集到 `dict_tuple` 里。
- 某个组合收集到两个下标后立即返回答案。
整体思想仍是哈希加速查找配对关系。

3. Code Walkthrough
- `dict_num` 用来记录某些值是否出现过（以及下标）。
- `key = (min(num, cha), max(num, cha))` 统一组合顺序，避免重复键。
- `dict_tuple[key]` 存这一对组合对应的下标列表。
- 当某个键长度达到 2，说明找到目标两数，直接返回。

4. Key Takeaways
- 两数之和最经典是“边遍历边查补数”哈希法。
- 当前实现可运行，但结构比标准解更复杂。
- 时间复杂度接近 O(n)，空间复杂度 O(n)。
- 简化版本通常只需一个 `value -> index` 字典即可。
"""
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