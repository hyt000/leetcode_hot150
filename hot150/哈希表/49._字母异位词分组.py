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


