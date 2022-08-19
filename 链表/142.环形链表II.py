# 题目都没咋看明白

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return     # 如果链表无环，则返回null

            fast, slow = fast.next.next, slow.next
            # 定义快慢指针，快指针走两步，慢指针走一步
            if fast == slow: break
            # 如果快指针和慢指针相遇，跳出 while 循环
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
        # 找到相等时的索引

