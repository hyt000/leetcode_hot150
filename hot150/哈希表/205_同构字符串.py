# 给定两个字符串 s 和 t ，判断它们是否是同构的。
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)
        if sl != tl:
            return False
        dict1 = {}
        dict2 = {}
        for i,j in zip(s,t):
            if i not in dict1 and j not in dict2:
                dict1[i] = j
                dict2[j] = i
            elif i in dict1 and j in dict2:
                if dict1[i] == j and dict2[j] == i:
                    continue
                else:
                    return False
            else:
                return False
        return True


