# -*- coding: utf-8 -*-
"""
@Project :python_basic knowledge 
@Time    : 2024/6/4 10:33
@Author  : Rao Zhi
@File    : 2864.最大二进制奇数.py
@email   : raozhi@mails.cust.edu.cn
@IDE     : PyCharm 
@描述    :
@detail  :
@infer   :
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num = []
        for elem in s:
            num.append(int(elem))
        num.sort()
        new_s = ''
        one_num = num.count(1)
        for idx, i in enumerate(num[::-1]):
            if idx < (one_num - 1):
                new_s += str(i)
            elif idx == len(num)-1:
                new_s += "1"
            else:
                new_s += "0"

        return new_s


slu = Solution()
s = "110110"
print(slu.maximumOddBinaryNumber(s))

