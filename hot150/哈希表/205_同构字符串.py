# 给定两个字符串 s 和 t ，判断它们是否是同构的。
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
"""
1. Problem Description
判断两个字符串是否同构：`s` 的每个字符都能稳定映射到 `t` 的某个字符，且映射必须一一对应。

2. Solution Approach
和“单词规律”同类型，使用双向映射：
- `dict1`：`s` 字符 -> `t` 字符。
- `dict2`：`t` 字符 -> `s` 字符。
- 扫描过程中同时校验两边一致性。

3. Code Walkthrough
- 先比较长度，不同直接 False。
- 遍历 `zip(s, t)`：
  - 都未出现：建立双向映射。
  - 都已出现：检查 `dict1[i] == j` 且 `dict2[j] == i`。
  - 只出现一边：冲突，返回 False。
- 扫描完成返回 True。

4. Key Takeaways
- 同构判断核心是“映射稳定 + 不同键不能撞同值”。
- 时间复杂度 O(n)，空间复杂度 O(n)。
- 常见坑：只校验单向映射会误判。
- 双向约束是处理双射关系的通用方法。
"""
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


