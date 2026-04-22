# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
"""
1. Problem Description
判断两个字符串是否互为字母异位词，也就是字符组成完全一致、顺序可以不同。

2. Solution Approach
这份代码用“排序后比较”：
- 分别把 `s` 和 `t` 排序。
- 排序结果一样，就说明字符和次数都一致。

3. Code Walkthrough
- `sort_s = sorted(s)`、`sort_t = sorted(t)`。
- 直接返回 `sort_s == sort_t` 的布尔结果。
- 逻辑非常短，但核心判断完整。

4. Key Takeaways
- 排序比较是最直观写法，容易写对。
- 时间复杂度 O(n log n)，空间复杂度 O(n)（排序临时开销）。
- 若追求线性时间，可改用哈希计数（O(n)）。
- 字符串“组成是否相同”通常就两路：排序 or 计数。
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)
        return sort_s == sort_t