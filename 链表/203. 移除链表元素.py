# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# # 双指针
# class Solution:
#     def removeElements(self, head, val):
#         while head and head.val == val:
#             head = head.next
#         pre, cur = head, head
#         while cur:
#             if cur.val == val:
#                 pre.next = cur.next
#             else:
#                 pre = cur
#             cur = cur.next
#         return head
#
#
# head = ListNode()
# val = 6
# Soga = Solution()
# Answer = Soga.removeElements(head, val)
# print(Answer)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         dummy_head = ListNode(next=head)  # 添加一个虚拟节点
#         cur = dummy_head
#         while (cur.next != None):
#             if (cur.next.val == val):
#                 cur.next = cur.next.next  # 删除cur.next节点
#             else:
#                 cur = cur.next
#         return dummy_head.next

import json


# # 双指针
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        pre, cur = head, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head

# 为什么返回head?
# return pre ——输入[1,2,3,5,2,2], val = 2   返回[5]


# # 虚拟头结点
# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         dummyHead = ListNode(-1, head)
#         cur = dummyHead
#         while cur.next:
#             if cur.next.val == val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next
#         return dummyHead.next

# 链接：https://leetcode.cn/problems/remove-linked-list-elements/solution/203-yi-chu-lian-biao-yuan-su-you-ya-di-gui-c-yu-ya/

# # 迭代法
# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         # 先判断头节点要不要删除
#         while head and head.val == val:  # head = [1,2,4,6,4,6,2] 的链表形式  # val = 6
#             head = head.next
#         if not head: return
#         # 开始迭代着删除非头节点的节点
#         pre = head
#         while pre.next:
#             if pre.next.val == val:
#                 pre.next = pre.next.next
#             else:
#                 pre = pre.next
#         return head


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):  # 把链表转换成了字符，然后通过列表显示出来
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io

    def readlines():

        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)  # line = [1,2,4,6,4,6,2]
            head = stringToListNode(line)  # 把输入的列表字符转成链表,返回的是头节点
            line = next(lines)  # 输入的val值，现在是val = 6
            val = int(line)

            ret = Solution().removeElements(head, val)

            out = listNodeToString(ret)  # 把链表转成列表样子的字符
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

# 运行-输入：[1,2,4,6,4,6,2] 回车再加 6 回车 输出结果
