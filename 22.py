# -*- coding: utf-8 -*-
"""
@Project ：python_basic knowledge 
@Time    : 2023/9/6 19:39
@Author  : Rao Zhi
@File    : 22.py
@email   : raozhi@mails.cust.edu.cn
@IDE     ：PyCharm 

"""


def permutations(arr):
    if len(arr) == 0:
        return [[]]

    results = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i + 1:]
        for p in permutations(rest):
            results.append([arr[i]] + p)
    return results


# 给定列表
my_list = [7, 2, 2, 5]

# 生成排列
permutation_list = permutations(my_list)

print(permutation_list)
