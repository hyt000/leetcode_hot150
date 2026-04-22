# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」 定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
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


