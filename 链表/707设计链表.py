class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None



class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        # index steps needed
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:


    def addAtTail(self, val: int) -> None:


    def addAtIndex(self, index: int, val: int) -> None:


    def deleteAtIndex(self, index: int) -> None:



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# get(index)：获取链表中第index个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为val 的节点追加到链表的最后一个元素。

# addAtIndex(index,val)：在链表中的第index个节点之前添加值为val的节点。
# 如果index等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。
# 如果index小于0，则在头部插入节点。

# deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。

