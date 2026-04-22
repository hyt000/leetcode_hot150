# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# 实现 MinStack 类:

# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
"""
1. Problem Description
实现一个栈，除了普通的 `push/pop/top`，还要能随时 O(1) 拿到当前最小值。

2. Solution Approach
双栈法：
- `stack` 正常存所有值。
- `_stack` 同步存“到当前位置为止的最小值”。
- 每次入栈时，把当前最小值也压到 `_stack` 对应位置。
- 每次出栈时，两边一起弹出，保证对齐。

3. Code Walkthrough
- `push`：比较 `val` 和 `_stack[-1]`，把更小的（或旧最小）压入 `_stack`。
- `pop`：`stack` 和 `_stack` 同时 `pop`。
- `top`：返回当前栈顶缓存 `top_num`。
- `getMin`：直接返回 `_stack[-1]`，因此是 O(1)。

4. Key Takeaways
- 要在 O(1) 得最小值，就需要额外结构记录历史最小。
- 各操作时间复杂度都 O(1)；空间复杂度 O(n)。
- 常见错误是只在遇到更小值时才压辅助栈，会导致出栈后最小值恢复困难。
- “主结构 + 同步辅助结构”是非常通用的设计模式。
"""
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