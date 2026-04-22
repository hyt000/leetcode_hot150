# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」 定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
"""
1. Problem Description
给一个正整数，不断把它替换成“各位数字平方和”。如果最终能变成 1，就是快乐数；如果陷入循环，就不是。

2. Solution Approach
哈希表判环：
- 每次计算下一状态 `平方和`。
- 用 `history` 记录出现过的中间结果。
- 如果出现过，说明进入循环，返回 `False`。
- 如果变成 1，返回 `True`。

3. Code Walkthrough
- `calculate_square_sum`：把数字转字符串逐位平方求和。
- 主流程先算一次 `ji`，然后循环更新。
- `if not history.get(ji)`：没见过就记录并继续。
- 否则说明重复出现，直接判定不是快乐数。

4. Key Takeaways
- 只要状态空间有限且会重复，就可以用“记录历史”检测循环。
- 时间复杂度近似 O(log n * 迭代次数)，空间复杂度 O(迭代状态数)。
- 常见坑：忘记把初始值或中间值加入历史，导致死循环。
- 这题也可用快慢指针做数字状态判环。
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        history = {n:1}
        ji = self.calculate_square_sum(n)

        if ji==1:
            return True
        while ji!=1:
            if not history.get(ji):

                history[ji]=1
                ji = self.calculate_square_sum(ji)
            else:
                return False
        return ji==1






    def calculate_square_sum(self, nums):
        b = list(str(nums))
        sum=0
        for i in b:
            sum+=int(i) ** 2
        return sum

if __name__ == '__main__':
    n = 2
    print(Solution().isHappy(n))


