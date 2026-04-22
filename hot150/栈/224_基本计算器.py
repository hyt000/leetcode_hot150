"""
1. Problem Description
实现一个基本计算器，输入是字符串表达式（有空格、括号、加减等），不能用 `eval`，要自己算出结果。

2. Solution Approach
这份代码是“栈 + 括号内先算”的思路：
- 扫描字符串，数字先拼接，多位数一起处理。
- 遇到 `(` 直接入栈；遇到 `)` 就把括号内内容弹出来计算成一个数，再压回栈。
- 最后再对剩余表达式做一次线性计算。

3. Code Walkthrough
- `stack` 存数字和运算符混合序列。
- `temp_num` 用来拼多位数字字符。
- `calculate_kuohao` 负责计算一个“无括号”表达式列表，处理一元负号等情况。
- `operate` 统一封装加减乘除运算（本题核心通常只需加减）。

4. Key Takeaways
- 处理表达式题时，先拆成“数字/符号解析”和“计算规则”两层最稳。
- 常见坑：空格、负号在开头、括号嵌套。
- 时间复杂度整体 O(n)，空间复杂度 O(n)（栈）。
- 通用模式：遇到右括号就“局部求值再压回”。
"""
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
class Solution:
    def calculate(self, s: str) -> int:
        a=list(s)
        stack = []
        temp_num = []
        length = len(a)
        for index,strs in enumerate(a) :
            if strs.strip()=='':
                if index == length-1:
                    if temp_num:
                        num_now = ''.join(temp_num)
                        stack.append(int(num_now))

                        temp_num=[]
                    continue
                else:
                    continue
            
            if strs=='(':
                stack.append('(')
                continue
            elif strs==')':
                if temp_num:
                    num_now = ''.join(temp_num)
                    stack.append(int(num_now))
                temp_num=[]
                calculate_list = []
                num = stack.pop()
                while num!='(':
                    calculate_list.append(num)
                    num = stack.pop()
                
                zheng_list = calculate_list[::-1]
                kuohao_redult = self.calculate_kuohao(zheng_list)
                stack.append(kuohao_redult)
                continue
            if strs.isdigit():
                temp_num.append(strs)
            else:
                if temp_num:
                    num_now = ''.join(temp_num)
                    print(num_now)
                    stack.append(int(num_now))
                stack.append(strs)
                temp_num=[]
            
        if len(stack)==1 and not temp_num:
            return stack[0]
        else:
            if temp_num:
                    num_now = ''.join(temp_num)
                    print(num_now)
                    stack.append(int(num_now))

            return self.calculate_kuohao(stack)


    def calculate_kuohao(self,zhenglist):
        '''
        计算括号内的表达式,
        返回一个result
        '''
        reverse_operator = False
        temp_num=[]
        temp_operator = []
        for index,num in enumerate(zhenglist):
            if num==''or num==' ':
                continue
            elif num=='-' and index==0: 
                reverse_operator = True
                

            elif isinstance(num,int):
                if reverse_operator:
                    reverse_operator =False
                    temp_num.append(-num)
                else:
                    temp_num.append(num)
                if len(temp_num)==1:
                    continue
                elif len(temp_num)==2:
                    num2 = temp_num.pop()
                    num1 = temp_num.pop()
                    operator = temp_operator.pop()
                    res = self.operate(num1=num1,num2=num2,operator=operator)
                    temp_num.append(res)
            else:
                temp_operator.append(num)
        return temp_num[0]
        


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
    s = "-2"
    a = Solution()
    print(a.calculate(s=s))