# 给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。

# 请你计算该表达式。返回一个表示表达式值的整数。

# 注意：

# 有效的算符为 '+'、'-'、'*' 和 '/' 。
# 每个操作数（运算对象）都可以是一个整数或者另一个表达式。
# 两个整数之间的除法总是 向零截断 。
# 表达式中不含除零运算。
# 输入是一个根据逆波兰表示法表示的算术表达式。
# 答案及所有中间计算结果可以用 32 位 整数表示。
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        operators_stack = []
        all_operators = ['+','-','*' , '/']
        for strs in tokens:
            if strs in all_operators:
                operators_stack.append(strs)
                num2 = int(num_stack.pop())
                num1 = int(num_stack.pop())
                result = self.operate(num1,num2,strs)
                num_stack.append(result)
            else:
                num_stack.append(int(strs))
        return num_stack[0]

    

    def operate(self,num1,num2,operator):
        match operator:
            case '+':
                return num1+num2
            case '-':
                return num1-num2
            case '*':
                return num1*num2
            case '/':
                ans = int(num1/num2)

                
                return ans 
if __name__=='__main__':
    a=["4","-2","/","2","-3","-","-"]
    b=Solution()
    print(b.evalRPN(a))

