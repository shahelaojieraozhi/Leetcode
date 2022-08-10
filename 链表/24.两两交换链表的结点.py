class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         dummy_head = ListNode(0, head)
#         cur = dummy_head
#         while cur.next and cur.next.next:
#             pre1 = cur.next     # 指向中间结点
#             pre2 = cur.next.next.next   # 指向下一组的第一个结点
#             cur.next = cur.next.next    #
#             cur.next.next = pre1
#             cur.next.next.next = pre2
#             cur = cur.next.next
#
#         return dummy_head.next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)
        pre = res

        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # pre，cur，post对应最左，中间的，最右边的节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return res.next


