# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class MyLinkedList:
#
#     def __init__(self):
#         self.size = 0
#         self.head = ListNode(0)
#
#     def get(self, index: int) -> int:
#         if (index < 0) and (index > self.size):
#             return -1
#         else:
#             p = self.head
#             for i in range(index + 1):
#                 p = p.next
#             return p.val
#
#     def addAtHead(self, val: int) -> None:
#         self.size += 1
#         ListNode(val, self.head)
#
#     def addAtTail(self, val: int) -> None:
#         # 在末尾加一个值为val的结点
#         self.size += 1
#         p = self.head
#         for i in range(self.size - 1):
#             p = p.next
#         ListNode(val, p)
#
#     def addAtIndex(self, index: int, val: int) -> None:     # -> 这是指定输出类型
#         # 在链表中的第 index 个节点之前添加值为 val 的节点。
#         # 如果 index 等于链表的长度，则该节点将附加到链表的末尾。
#         # 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
#         if index == self.size:
#             self.addAtTail(val)
#             self.size += 1
#         if index > self.size:
#             return self.head
#         if index < 0:
#             self.addAtHead(val)
#             self.size += 1
#
#     def deleteAtIndex(self, index: int) -> None:
#         # 如果索引 index 有效，则删除链表中的第 index 个节点。
#         if (index < 0) and (index > self.size):
#             return self.head
#         else:
#             for i in range(index):
#                 self.head = self.head.next
#             self.head = self.head.next.next
#             self.size -= 1
#
#
# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
# linkedList.addAtTail(3)
# linkedList.addAtIndex(1, 2)
# linkedList.get(1)
# linkedList.deleteAtIndex(1)
# linkedList.get(1)
'''
链表的关键：在遍历时一定要搞个临时指针，直接对链表操作会改变链表
增加新的结点时，先定义一个Node先配置它的前后指针
'''


# 出现问题：为什么我的最后输出的是2，我手动单步执行感觉也是3啊
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # 虚拟头部节点

    def get(self, index: int) -> int:
        if (index < 0) and (index > self.size):
            return -1
        else:
            cur = self.head.next
            while index:
                cur = cur.next
                index -= 1
            return cur.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # 在末尾加一个值为val的结点
        node = ListNode(val)
        cur = self.head

        while self.size > 0:
            cur = cur.next
            self.size -= 1
        cur.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:  # -> 这是指定输出类型
        # 在链表中的第 index 个节点之前添加值为 val 的节点。
        # 如果 index 等于链表的长度，则该节点将附加到链表的末尾。
        # 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
        if index == self.size:
            self.addAtTail(val)
            self.size += 1
        if index > self.size:
            return
        if index < 0:
            self.addAtHead(val)
            self.size += 1
        else:
            cur = self.head.next
            node = ListNode(val)
            i = 0
            while i < index - 1:
                cur = cur.next
                i += 1
            node.next = cur.next
            cur.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # 如果索引 index 有效，则删除链表中的第 index 个节点。
        if (index < 0) and (index > self.size):
            return
        else:
            cur = self.head.next
            while index - 1 > 0:
                cur = cur.next
            cur.next = cur.next.next
            self.size -= 1


# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
# linkedList.addAtTail(3)
# linkedList.addAtHead(1)
# linkedList.addAtIndex(5, 2)
# linkedList.deleteAtIndex(1)
# print(linkedList.get(1))


linkedList = MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)
print(linkedList.get(1))
linkedList.deleteAtIndex(1)
print(linkedList.get(1))

# 朴素一点的解法
# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
#
# # 参考 https://leetcode.cn/problems/design-linked-list/solution/xiao-bai-chang-gui-jie-fa-by-ji-bai-yu-shi-ta/
#
# class MyLinkedList:
#
#     def __init__(self):
#         self.head = Node(None)
#
#     def get(self, index: int) -> int:
#         if index < 0:
#             return -1
#         p = self.head.next
#         for i in range(index):
#             if p.next is None:
#                 return -1
#             p = p.next
#         return p.val
#
#     def addAtHead(self, val: int) -> None:
#         node = Node(val)
#         node.next = self.head.next
#         self.head.next = node
#         # Node(val, self.head)
#
#     def addAtTail(self, val: int) -> None:
#         p = self.head
#         while p.next is not None:
#             p = p.next
#         p.next = Node(val)
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         p = self.head
#         if index < 0:
#             self.addAtHead(val)
#         for i in range(index):
#             if p.next is None:
#                 return
#             p = p.next
#         node = Node(val)
#         node.next = p.next
#         p.next = node
#
#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0:
#             return
#         p = self.head
#         for i in range(index):
#             if p.next is Node:
#                 return
#             p = p.next
#         try:
#             p.next = p.next.next
#         except:
#             p.next = None
#
#
# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
# linkedList.addAtTail(3)
# linkedList.addAtIndex(1, 2)
# linkedList.get(1)
# linkedList.deleteAtIndex(1)
# linkedList.get(1)
# print(linkedList.get(1))
