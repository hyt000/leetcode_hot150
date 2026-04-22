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