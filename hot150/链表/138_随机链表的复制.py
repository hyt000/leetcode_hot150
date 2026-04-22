##重做！最好时间复杂度是O(N)
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

# 返回复制链表的头节点。

# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

#思考：先把原始的保存到字典中，按照序号保存
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        origin_list= []
        point_index_list = []
        list_result = []
        been_pointed = []
        i=0
        dummy = Node(0)
        res = dummy
        count = 0
        while head:
            
            origin_list.append(head)
            res.next = Node(head.val)
            res = res.next
            
            head = head.next
            list_result.append(res)
        list_result.append(None)
            
        for i in range(len(origin_list)):
            if origin_list[i].random:
                index_random = origin_list.index(origin_list[i].random)
            else:
                index_random = -1
            list_result[i].random = list_result[index_random]
        return dummy.next
        

# 3. 手动构建测试用例: [[7,null],[13,0],[11,4],[10,2],[1,0]]
def test():
    # 第一步：创建所有节点（先不连指针）
    node0 = Node(7)
    node1 = Node(13)
    node2 = Node(11)
    node3 = Node(10)
    node4 = Node(1)

    # 第二步：连接 next 指针
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None

    # 第三步：连接 random 指针
    node0.random = None    # [7, null]
    node1.random = node0   # [13, 0] -> 指向索引 0
    node2.random = node4   # [11, 4] -> 指向索引 4
    node3.random = node2   # [10, 2] -> 指向索引 2
    node4.random = node0   # [1, 0]  -> 指向索引 0

    # 第四步：调用你的实现
    sol = Solution()
    res = sol.copyRandomList(node0)

    # 第五步：简单的打印验证
    print("--- 复制结果验证 ---")
    curr = res
    idx = 0
    nodes = [] # 存储新节点方便查看索引
    temp = res
    while temp:
        nodes.append(temp)
        temp = temp.next

    curr = res
    while curr:
        random_val = curr.random.val if curr.random else "null"
        # 查找 random 指向的节点在链表中的索引
        random_idx = nodes.index(curr.random) if curr.random in nodes else "External/Error"
        print(f"Node {idx}: val={curr.val}, random_val={random_val}, random_idx={random_idx}")
        curr = curr.next
        idx += 1

if __name__ == "__main__":
    test()
        