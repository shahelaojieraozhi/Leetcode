# -*- coding: utf-8 -*-
"""
@Project ：python_basic knowledge 
@Time    : 2024/5/10 10:36
@Author  : Rao Zhi
@File    : 232.用栈实现队列.py
@email   : raozhi@mails.cust.edu.cn
@IDE     ：PyCharm 
@描述     :
@detail   ：
@infer    :
"""
import pylab as p


class MyQueue:

    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        peek = self.peek()
        self.B.pop()
        return peek

    def peek(self) -> int:
        if self.B: return self.B[-1]
        if not self.A: return -1
        # 将栈 A 的元素依次移动至栈 B
        while self.A:
            self.B.append(self.A.pop())
        return self.B[-1]

    def empty(self) -> bool:
        return not self.A and not self.B


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(3)
    q.push(5)
    print(q.pop())  # 1
    print(q.pop())  # 3
    print(p.empty)
