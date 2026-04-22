#列表不可哈希，元组可以

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = []
#         for str in strs:
#             if not res:
#                 res.append([str])
#                 continue
#             for valid_list in res:
#                 flag = False
#                 if self.valid_word(str,valid_list[0]):
#                     valid_list.append(str)
#                     flag = True
#                     break
#             if not flag:
#                     res.append([str])
#         return res
#
#
#
#
#
#     def valid_word(self, s: str,t:str) -> bool:
#         dict_c = {}
#         for c in s:
#             dict_c[c] = dict_c.get(c, 0) + 1
#         for c in t:
#             dict_c[c] = dict_c.get(c, 0) - 1
#         for val in dict_c.values():
#             if val != 0:
#                 return False
#         return True








#append没有返回值
"""
1. Problem Description
把一组字符串按“字母异位词”分组。异位词就是字符种类和次数都一样，只是顺序不同。

2. Solution Approach
核心是“标准化 key”：
- 对每个单词排序，得到规范形式（如 `eat/tea/ate` 都变成 `aet`）。
- 用这个规范字符串当哈希键，把原单词分到同一组。

3. Code Walkthrough
- `sortword = ''.join(sorted(word))` 生成分组键。
- `dict_[sortword] = [word]` 初始化新组。
- 已存在就 `append` 到对应组。
- 最后 `list(dict_.values())` 返回所有分组结果。

4. Key Takeaways
- “把等价对象映射为同一个 key”是哈希分组题的通用套路。
- 时间复杂度约 O(n * k log k)，k 是单词平均长度（排序开销）。
- 空间复杂度 O(nk)（存储分组结果）。
- 如果字符集固定（如仅小写字母），也可用计数数组当 key 做优化。
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        for word in strs:
            sortword = ''.join(sorted(word))
            if   dict_.get(sortword)==None:
                dict_[sortword] = [word]

            else:
                dict_[sortword].append(word)
        return list(dict_.values())

if __name__ == '__main__':
    strs =["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))


