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