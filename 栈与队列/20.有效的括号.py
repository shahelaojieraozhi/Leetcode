# -*- coding: utf-8 -*-
"""
@Project ：python_basic knowledge 
@Time    : 2024/5/10 10:48
@Author  : Rao Zhi
@File    : 20.有效的括号.py
@email   : raozhi@mails.cust.edu.cn
@IDE     ：PyCharm 
@描述     :
@detail   ：
@infer    :
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:     # 如果 stack 不为空且stack最底下的元素不等于待匹配的元素
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


if __name__ == '__main__':
    sol = Solution()
    s = "[]({}[])"
    print(sol.isValid(s))
