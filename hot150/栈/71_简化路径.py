# 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为 更加简洁的规范路径。
#
# 在 Unix 风格的文件系统中规则如下：
#
# 一个点 '.' 表示当前目录本身。
# 此外，两个点 '..' 表示将目录切换到上一级（指向父目录）。
# 任意多个连续的斜杠（即，'//' 或 '///'）都被视为单个斜杠 '/'。
# 任何其他格式的点（例如，'...' 或 '....'）均被视为有效的文件/目录名称。
# 返回的 简化路径 必须遵循下述格式：
#
# 始终以斜杠 '/' 开头。
# 两个目录名之间必须只有一个斜杠 '/' 。
# 最后一个目录名（如果存在）不能 以 '/' 结尾。
# 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
# 返回简化后得到的 规范路径 。
"""
1. Problem Description
给一个 Unix 绝对路径，里面可能有 `.`、`..`、多余 `/`，要化成标准路径。

2. Solution Approach
用栈模拟目录层级：
- 按 `/` 切分路径段。
- 空串和 `.` 直接忽略。
- `..` 表示回到上一级：栈不空就弹出一个目录。
- 普通目录名就入栈。
- 最后用 `/` 把栈中目录拼回去。

3. Code Walkthrough
- `for strs in path.split('/')`：逐段处理。
- `if strs=='' or strs=='.'`：跳过无效段。
- `elif strs=='..'`：执行回退（`pop`）。
- 否则 `stack.append(strs)` 存目录名。
- 结果是 `'/' + '/'.join(stack)`。

4. Key Takeaways
- 路径规范化本质是一个“进目录/退目录”的栈问题。
- 时间复杂度 O(n)，空间复杂度 O(n)。
- 常见坑：根目录下再 `..` 不应继续退。
- 看到层级回退语义（括号、目录、撤销）就优先想栈。
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for strs in path.split('/'):
            if strs=='':
                continue
            else:
                if strs=='.':
                    continue
                elif strs=='..':
                    if not stack:
                        stack = '/'
                    stack.pop()
                else:
                    stack.append(strs)
        res ='/'+ '/'.join(stack)
        return res
if __name__=='__main__':
    path = "/a/../../b/../c//.//"
    a = Solution()
    print(a.simplifyPath(path=path))

















