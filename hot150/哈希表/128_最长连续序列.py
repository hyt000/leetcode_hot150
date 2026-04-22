# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""
1. Problem Description
给一个无序整数数组，找出最长的“连续数字序列”长度。连续序列不要求在原数组里位置连续，只要值连续即可。

2. Solution Approach
这份代码思路是“去重 + 排序 + 扫描”：
- 先 `set` 去重，再排序。
- 线性扫描统计当前连续段长度。
- 一旦断开，就更新最大长度并重置当前段。
注意：题目理想要求 O(n)，这版因为排序是 O(n log n)。

3. Code Walkthrough
- `nums = sorted(list(set(nums)))`：去重并排序。
- `list_` 暂存当前连续段，`max_len` 记录历史最大。
- 若 `num == 上一个 + 1`，加入当前段；否则结算并重开新段。
- 循环后再做一次 `max`，处理最后一段。

4. Key Takeaways
- 连续序列问题常见两路：排序扫一遍，或哈希集合 O(n)。
- 这版时间复杂度 O(n log n)，空间复杂度 O(n)。
- 常见坑：重复元素会干扰连续判断，所以先去重很关键。
- 若追求最优，可用“只从序列起点开始扩展”的集合法。
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1

        dict_num={}
        nums = sorted(list(set(nums)))
        list_=[nums[0]]
        index_=0
        max_len=1
        for num in nums[1:]:
            if num==list_[index_]+1:
                list_.append(num)
                index_+=1
            else:
                now = len(list_)
                max_len = max(max_len,now)
                list_ = [num]
                index_ = 0
        max_len=max(max_len,index_+1)
        return max_len

if __name__ == '__main__':
    nums =[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(Solution().longestConsecutive(nums))