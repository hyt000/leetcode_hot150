# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
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