# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 与Carl给的答案思路相仿，但是每次迭代的是重新创造一个新的结点
# 在Leedcode跑不了，报错：No .val
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = ListNode(cur.val)
        while cur:
            cur = cur.next
            temp = ListNode(cur.val)
            temp.next = pre
            pre = temp
        return pre


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while (cur != None):
            temp = cur.next  # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre  # 反转
            # 更新pre、cur指针
            pre = cur
            cur = temp
        return pre
