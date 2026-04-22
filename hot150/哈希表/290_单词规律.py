# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。具体来说：
#
# pattern 中的每个字母都 恰好 映射到 s 中的一个唯一单词。
# s 中的每个唯一单词都 恰好 映射到 pattern 中的一个字母。
# 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        t = list(pattern)
        sl = len(s)
        if sl != len(pattern):
            return False
        dict1 = dict()
        dict2 = dict()

        for i, j in zip(s, t):
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


