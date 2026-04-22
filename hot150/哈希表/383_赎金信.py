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
