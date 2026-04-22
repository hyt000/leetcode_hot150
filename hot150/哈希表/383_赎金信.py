# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 如果可以，返回 true ；否则返回 false 。
# magazine 中的每个字符只能在 ransomNote 中使用一次。
# 示例 1：
# 输入：
# ransomNote = "a", magazine = "b"
# 输出：
# false
# 示例 2：
# 输入：
# ransomNote = "aa", magazine = "ab"
# 输出：
# false
# 示例 3：
# 输入：
# ransomNote = "aa", magazine = "aab"
# 输出：
# true



"""
1. Problem Description
判断 `ransomNote` 能不能由 `magazine` 里的字符拼出来；`magazine` 每个字符最多只能用一次。

2. Solution Approach
字符计数哈希：
- 先统计 `magazine` 每个字符出现次数。
- 再遍历 `ransomNote`，每需要一个字符就把对应计数减 1。
- 如果某字符不存在或数量不够，直接返回 False。

3. Code Walkthrough
- `all_str[string] = all_str.get(string, 0) + 1`：构建库存。
- 遍历赎金信字符：
  - `if string not in all_str`：完全没有该字符，失败。
  - `if all_str[string] == 0`：库存耗尽，失败。
  - 否则 `all_str[string] -= 1`。
- 全部通过返回 True。

4. Key Takeaways
- 这是非常典型的“供需匹配 + 计数器”问题。
- 时间复杂度 O(m+n)，空间复杂度 O(k)（k 为字符种类数）。
- 常见坑：只判断是否存在，不判断次数。
- 字符频次题优先考虑哈希计数（或 `Counter`）。
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        all_str = {}
        for string in magazine:
            all_str[string] = all_str.get(string, 0) + 1
        for string in ransomNote:
            if string not in all_str:
                return False
            else:
                if all_str[string] == 0:
                    return False
                all_str[string] -= 1
        return True

if __name__ == '__main__':
    ransomNote = 'aa'
    magazine = 'aab'
    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)
    print(result)
