# -*- coding: utf-8 -*-
"""
@Project ：python_basic knowledge 
@Time    : 2024/5/11 10:42
@Author  : Rao Zhi
@File    : 504.7进制转换.py
@email   : raozhi@mails.cust.edu.cn
@IDE     ：PyCharm 
@描述     :
@detail   ：
@infer    :
"""


# class Solution:
#     def convertToBase7(self, num: int) -> str:
#         stack = []
#         # if res in base:
#         #     stack.append(res)
#         # else:
#         #     res = num % 7
#         #     convertToBase7(num // 7)
#         if num == 0:
#             return "0"
#         if num < 0:
#             num = -num
#             while num > 0:
#                 rem = num % 7
#                 stack.append(rem)
#                 num = num // 7
#             print("进栈后:", stack)
#             s = "-"
#             while stack:
#                 s = s + str(stack.pop())
#         else:
#             while num > 0:
#                 rem = num % 7
#                 stack.append(rem)
#                 num = num // 7
#             print("进栈后:", stack)
#             s = ""
#             while stack:
#                 s = s + str(stack.pop())
#         return s
#
#
# s = Solution()
# print(s.convertToBase7(102))


# leetcode 最快的答案
# class Solution:
#     def convertToBase7(self, num: int) -> str:
#         n = '-' if num < 0 else ''
#         result = ''
#         num = abs(num)
#         while num > 0:
#             result += str(num % 7)
#             num //= 7
#         return n + ''.join(result[::-1]) if result else '0'
#
#
# s = Solution()
# print(s.convertToBase7(102))


class Solution:
    def convertToBase7(self, num: int) -> str:
        s = "" if num > 0 else "-"
        res = ""
        num = abs(num)
        while num > 0:
            res += str(num % 7)
            num = num // 7
        return s + res[::-1] if res else "0"


s = Solution()
print(s.convertToBase7(-102))
