"""
1. Problem Description
这题要实现一个 LRU 缓存：数据满了以后，最久没用的键值对要被淘汰。并且 `get/put` 都要求尽量快（理想是 O(1)）。

2. Solution Approach
这份代码用的是“哈希表 + 时间戳”思路：
- `cache` 存 key -> value。
- `recent_use` 存 key -> 最近访问时间。
- 每次 `get/put` 都让 `times += 1`，更新该 key 的最近时间。
- 容量满时，用 `min(recent_use)` 找最久未使用的 key 并删除。
注意：这里淘汰时用了 `min`，所以这一版 `put` 在满容量时是 O(n)，不满足题目最优 O(1) 要求。

3. Code Walkthrough
- `__init__`：初始化容量、剩余空间、两个字典和时间计数器。
- `get`：命中就刷新时间并返回值，没命中返回 -1。
- `put`：
  - key 已存在：更新 value，并刷新最近使用时间。
  - key 不存在且有空位：直接插入。
  - key 不存在且已满：找最小时间戳对应 key，先删再插入新 key。

4. Key Takeaways
- LRU 的本质是“既要快查 key，又要快维护新旧顺序”。
- 这版时间复杂度：`get` 平均 O(1)，满容量时 `put` 是 O(n)。
- 若要严格 O(1)，常见模式是“哈希表 + 双向链表”。
- 实战里要重点区分“能跑通”和“满足复杂度约束”。
"""
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.rest_capacity = capacity
        self.cache = {}
        self.recent_use={}
        self.times = 0
    def get(self, key: int) -> int:
        if key in self.cache:
            self.times += 1
            self.recent_use[key] = self.times
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.times += 1
            self.recent_use[key] = self.times
            self.cache[key] = value
        else:
            if self.rest_capacity > 0:
                self.cache[key] = value
                self.times += 1
                self.recent_use[key] = self.times
                self.rest_capacity -= 1
            else:
                #找到最小的对应的key
                min_key = min(self.recent_use, key=self.recent_use.get)
                self.recent_use.pop(min_key)
                self.cache.pop(min_key)
                self.times += 1
                self.recent_use[key] = self.times
                self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
第一句

我要用字典快速找 key

第二句

我要用双向链表维护最近使用顺序

第三句

谁被访问了，谁就移到头部

第四句

满了就删尾部，因为尾部最久没用'''