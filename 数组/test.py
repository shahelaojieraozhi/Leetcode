# nums = [-4, -1, 0, 3, 10]
# res = [-1] * len(nums)

# lis0 = []
# lis1 = [1, 2, 3]
# lis2 = [2, 3, 4]
#
# lis0.append(lis1)
# lis0.append(lis2)
# print(lis0)
#
#
# result = [[], [], []]
# result[1].append(1)
# result[2].append(3)
# print(result)

# result = []
# for i in range(10):
#     result.append([])
# print(result)

# lis = [[1, 2, 3], [4, 2], [1]]
# L = []
# for i in range(len(lis)):
#     L.append(len(lis[i]))
# print(min(L))

# lis1 = []
# n = 4
# for i in range(n):
#     lis1.append(i + 1)
# print(lis1)
# lis2 = lis1
# for i in range(len(lis1)):
#     lis2[i] = lis1[i] + 3
# print(lis2)


# n = 3
# mat = [[0 for _ in range(n)] for _ in range(n)]
# print(mat)
# lis = []
# lis2 = []
# for i in range(3):
#     lis.append(0)
# for j in range(3):
#     lis2.append(lis)
# print(lis2)

# lis = []
# for i in range(4, 0, -1):
#     lis.append(i)
# print(lis)
# # [4, 3, 2, 1]


# lis = list(s)
# lis2 = list(s)
# lis2.reverse()
# print(lis2)
# print(''.join(lis))


# s = "a-bC-dEf-ghIj"
# lis = list(s)
# lis2 = list(s)
# lis2.reverse()
# L = len(lis)
# lis3 = []
# lis4 = list(s)
# for i in range(L):
#     if lis2[i].isalpha() == True:
#         lis3.append(lis2[i])
# print(lis3)
#
# fast, slow = 0, 0
# while fast < len(lis):
#     if lis[fast].isalpha() == True:
#         lis[fast] = lis3[slow]
#         slow += 1
#     fast += 1
# print(lis)


# result = [-1] * 5
# print(result)
# print(type(result))

# s = "ADOBECODEBANC"
# ls_s = list(s)
# t = "ABC"
# ls_t = list(t)
# ls = []
#
# for i in range(8):
#     ls.append(ls_s[i])
# flag = 0
# for char1 in ls_s:
#     for char2 in ls_t:
#         if char1 == char2 and flag <= 2:
#             flag += 1
#
# print(flag)

# window = [1, 2, 3, 4]
# ls_s = [2, 3, 4]
# window.remove(ls_s[2])
# print(window)


# from collections import *
#
# string = "abcdedgaabbccdd"
# out = Counter(string)
# print(out)
# # Counter({'d': 4, 'a': 3, 'b': 3, 'c': 3, 'e': 1, 'g': 1})

# from collections import *
#
# members = [
#     ['male', 'John'],
#     ['male', 'Jack'],
#     ['female', 'Lily'],
#     ['male', 'Pony'],
#     ['female', 'Lucy']
# ]
#
# d = defaultdict(list)
# for sex, name in members:
#     d[sex].append(name)
#
# print(d)
# # defaultdict(<class 'list'>, {'male': ['John', 'Jack', 'Pony'], 'female': ['Lily', 'Lucy']})


# from collections import defaultdict

#
# l = [('a', 2), ('b', 3), ('a', 1), ('b', 4), ('a', 3), ('a', 1), ('b', 3)]
# d = defaultdict(list)
# for key, value in l:
#     d[key].append(value)
# print(d)
# # defaultdict(<class 'list'>, {'a': [2, 1, 3, 1], 'b': [3, 4, 3]})


# d = defaultdict(set)
# for key, value in l:
#     d[key].add(value)
# print(d)
# # defaultdict(<class 'set'>, {'a': {1, 2, 3}, 'b': {3, 4}})

# from collections import defaultdict
#
#
# sen = 'hello world'
# d = defaultdict(int)
# for key in sen:
#     d[key] += 1
# print(d)
# # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


# seq = ['one', 'two', 'three']
# print(list(enumerate(seq)))
# # [(0, 'one'), (1, 'two'), (2, 'three')]
# for i, element in enumerate(seq):
#     print(i, element)
# # 0 one
# # 1 two
# # 2 three

# s = "ADOBEC"
# print(list(enumerate(s, 0)))
# # [(0, 'A'), (1, 'D'), (2, 'O'), (3, 'B'), (4, 'E'), (5, 'C')]
# for j, c in enumerate(s, 9):
#     print(j, c)
# # 9 A
# # 10 D
# # 11 O
# # 12 B
# # 13 E
# # 14 C

from collections import defaultdict

# sen = "ADOBECODEBANC"
# d = defaultdict(int)
# for key in sen:
#     d[key] += 1
# print(d['A'])

from collections import *

s = "ADOBECODEBANC"

# t = "ABC"
# new_string = s[1:]
# print(new_string)
#
# ans = float('inf')
# start, end = 0, 0
# n = len(s)
# ls_s = list(s)
# ls_t = list(t)
# window = []
#
# for end in range(9):
#     window.append(ls_s[end])
# out_t = Counter(ls_t)
# out_window = Counter(window)
# for j in enumerate(s[9:],2):
#     print(j)

# for j, c in enumerate(s[9:], 6):
#     print(j, c)
# print(out_t)
# print(out_window)

# s = "a-bC-dEf-ghIj"
# lis_s = list(s)
# print(lis_s)
# print(''.join(lis_s))

# fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
# dir = Counter(fruits)
# print(dir)      # Counter({3: 5, 1: 3, 2: 2, 4: 1})
# print(len(dir))     # 4
# print(dir[3])   # 5


# li = [1, 2, 3, 4, 5]  # 列表本身不包含数据1,2,3,4,5，而是包含变量：li[0] li[1] li[2] li[3] li[4]
# first = li[0]  # 拷贝列表，也不会有数据对象的复制，而是创建新的变量引用
# del li[0]
# print(li)  # 输出[2, 3, 4, 5]
# print(first)  # 输出 1

# nums = [1, 12, -5, -6, 50, 3]
# print(nums[:4])    # 前四个
# print(nums[1:])     # [12, -5, -6, 50, 3]
# print(nums[:])
#
# total = sum(nums[:4])
# print(total)

# set1 = {'A', 'B', 'C'}
# set1.add('D')
# print(set1)
# set1.add('D')
# print(set1)
#
# set1.remove('A')
# print(set1)


# # 重复否？
# def finddif(s):
#     set1 = set()
#     for c in s:
#         set1.add(c)
#     return False if len(set1) < len(s) else True
#
# s = 'ABCDD'
# print(finddif(s))

# s1 = "abcabcbb"
# s = s1[:3]
# print(s)

# s = " "
# s1 = ' '
# print(len(s))
# print(len(s1))

# for i in range(3):
#     print()
#     for j in range(4):
#         print("*", end='')

# num1 = lambda n: n ** 2
# print(num1(3))

# maxtix1 = [[0 for _ in range(3)] for _ in range(3)]
# print(maxtix1)

# import collections
#
# s = "dddccdbba"
# print(collections.Counter(s))

# coding=utf-8
# import collections
#
# queue = collections.deque()
# queue.append('a')
# queue.append('b')
# queue.append('c')
# print(queue)
# queue.appendleft('A')
# queue.appendleft('B')
# print(queue)

# num_sorted = []
# P2 = 3
# nums2 = [1, 2, 3, 0, 0, 0]
# num = num_sorted + nums2[P2:]
# print(num)

import numpy as np

# a = np.arange(10)
#
# for i in a[::-1]:
#     print(i)

# nums1 = [1, 2, 3, 4, 5]
#
# print(nums1[:0])

digits = [3, 1, 2]
# L = len(digits)
# num = 0
# shuwei = 1
# for i in range(L):
#     for j in range((L - i - 1)):
#         shuwei *= 10
#     num += (digits[i] * shuwei)
#     shuwei = 1
#
# print(num)
#
# lis_ = list(str(num))
# print(lis_)
# print(int(lis_[0]))
# lis = []
# for i in lis_:
#     lis.append(int(i))
# print(lis)

# str1 = []
# for element in digits:
#     str1 += str(element)
# num = int(''.join(str1))
# print(num)

# a = 899
#
# print(str(a))
# b = [int(i) for i in str(a)]
# print(b)

# lis = [1, 2, 3, 4]
# lis[:2] = 0
# print(lis)

# arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
# slow = fast = 0
# inx_list = []
# index = 0
# while slow < len(arr):
#     if arr[fast] <= arr[slow]:
#         index += 1
#     fast += 1
#     if fast >= len(arr):
#         inx_list.append(index)
#         slow += 1
#         index = 0
#
# print(inx_list)

# print(min(arr))

arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
# n = len(arr)
# idx_lis = []
# num = 0
# for i in range(n):
#     idx = 1
#     for j in range(n):
#         if arr[i] > arr[j]:
#             idx += 1
#         elif arr[i] == arr[j] and i != j:
#             # 前i个全部 -1
#             num += 1
#
#     idx_lis.append(idx)
#
# for k in range(len(idx_lis)):
#     idx_lis[k] = idx_lis[k] - (num//2)
#
# print(idx_lis)


# print(sorted(set(arr)))
# map1 = sorted(set(arr))
# map2 = {}
# for idx, element in enumerate(map1, 1):
#     map2[element] = idx
# print(map2)
# lis = [map2[v] for v in arr]
# print(lis)
#
#
# def arrayRankTransform(arr):
#     ranks = {element: idx for idx, element in enumerate(sorted(set(arr)), 1)}
#     return [ranks[v] for v in arr]
#
#
# print(arrayRankTransform(arr))
