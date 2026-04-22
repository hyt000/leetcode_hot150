# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# 实现 MinStack 类:

# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
class MinStack:

    def __init__(self):
        self.top_num=None
        self.stack = list()
        self._stack=list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self._stack:
            self._stack.append(val)
        else:
            if self._stack[-1]<val:
                self._stack.append(self._stack[-1])
            else:
                self._stack.append(val)
        self.top_num=val
        

    def pop(self) -> None:
        last_one = self.stack.pop()
        self._stack.pop()
        if not self._stack:
            self.top_num=None
        else:
            self.top_num=self.stack[-1]

    def top(self) -> int:
        return self.top_num
        
    def getMin(self) -> int:
        return self._stack[-1]
    
if __name__=='__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()