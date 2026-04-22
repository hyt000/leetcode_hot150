# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。具体来说：
#
# pattern 中的每个字母都 恰好 映射到 s 中的一个唯一单词。
# s 中的每个唯一单词都 恰好 映射到 pattern 中的一个字母。
# 没有两个字母映射到同一个单词，也没有两个单词映射到同一个字母。
"""
1. Problem Description
给一个模式串 `pattern` 和一句话 `s`，判断它们是否一一对应：
每个模式字符映射一个单词，每个单词也只能映射一个模式字符。

2. Solution Approach
双向哈希映射：
- `dict1` 记录单词 -> 模式字符。
- `dict2` 记录模式字符 -> 单词。
- 扫描时两边都要一致，任何一边冲突都返回 False。

3. Code Walkthrough
- 先 `s.split(' ')`，并检查长度是否和 `pattern` 一样。
- 遍历 `zip(s, pattern)`：
  - 两边都没见过：建立新映射。
  - 两边都见过：检查映射是否互相匹配。
  - 只一边见过：直接冲突，返回 False。
- 全部通过返回 True。

4. Key Takeaways
- 这题重点是“双向唯一”，不是单向包含。
- 时间复杂度 O(n)，空间复杂度 O(n)。
- 常见坑：只建一个映射会漏掉“两个字符映射同一个单词”的冲突。
- 凡是要求双射/一一对应，基本都要双哈希。
"""
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


