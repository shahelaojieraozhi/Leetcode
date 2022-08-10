import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# [1,2,3,4,5]
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int):
        dummy_head = ListNode(next=head)  # 添加一个虚拟节点
        cur = dummy_head
        length_Node = 0
        while head:
            length_Node += 1
            head = head.next

        times = length_Node - n
        for i in range(1, times):
            cur = cur.next  # 这是遍历
        cur.next = cur.next.next    # 而这是赋值

        return dummy_head.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         def getLength(head: ListNode) -> int:
#             length = 0
#             while head:
#                 length += 1
#                 head = head.next
#             return length
#
#         dummy = ListNode(0, head)
#         length = getLength(head)
#         cur = dummy
#         for i in range(1, length - n + 1):
#             cur = cur.next
#         cur.next = cur.next.next
#         return dummy.next



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


def listNodeToString(node):
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
            line = next(lines)
            head = stringToListNode(line)
            line = next(lines)
            n = int(line)

            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()



