# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，
# 满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false

from typing import List
# num in dict（键存在性判断）和 dict.get(num)时间复杂度均为 O (1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_num={}
        for index,num in enumerate(nums):
            if num in dict_num:
                if abs(dict_num[num]-index)<=k:
                    return True
                else:
                    dict_num[num]=index
            else:
                    dict_num[num]=index

        return False

if __name__ == '__main__':
    nums = [1, 2, 3, 1,2,3]
    k = 2
    a = Solution()
    ans = a.containsNearbyDuplicate(nums, k)
    print(ans)


