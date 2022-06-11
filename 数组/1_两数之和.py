# Python
# # 类内函数的调用
# class Solution(object):
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return i, j
#
#
# Soga = Solution()
# # nums = [2, 7, 11, 15]
# # target = 9
# print(Soga.twoSum([2, 7, 11, 15], 18))

# # 自己通过哈希表写的：
# dict1 = {0: 2, 1: 7, 2: 11, 3: 11}
# # print(dict1[2])
# target = 9
# len1 = len(dict1)
#
# for i in range(len1):
#     for j in range(i + 1, len1):
#         if (target - dict1[i]) == dict1[j]:
#             print(i, j)


# enumerate在字典上是枚举、列举的意思
# 如果对一个列表，既要遍历索引又要遍历元素时，首先可以这样写：

# list1 = ['这', '是', '一个', '测试']
# for i in range(len(list1)):
#     print(i, list1[i])
# # 0 这
# # 1 是
# # 2 一个
# # 3 测试

# list1 = ['这', '是', '一个', '测试']
# for index, item in enumerate(list1):
#     print(index, item)
# # 0 这
# # 1 是
# # 2 一个
# # 3 测试

# enumerate还可以接收第二个参数，用于指定索引起始值，如：
# for index, item in enumerate(list1, 1):
#     print(index, item)
# # 1 这
# # 2 是
# # 3 一个
# # 4 测试

# # 如果要统计文件的行数，可以这样写：
# count = 0
# for index, line in enumerate(open(r'E:\code\python_code\python基础\python储备/ACO.txt', 'r')):
#     count += 1
# print(count)


# # 网上的答案：
# def two_sum(nums, target):
#     """这样写更直观，遍历列表同时查字典"""
#     dct = {}
#     for i, n in enumerate(nums):
#         cp = target - n
#         if cp in dct:
#             return [dct[cp], i]
#         else:
#             dct[n] = i
#
#
# print(two_sum([2, 7, 11, 15], 9))

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
# 以下是 enumerate() 方法的语法:
#
# enumerate(sequence, [start=0])


# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
#
# print(list(enumerate(seasons, start=1)))    # 下标从 1 开始
# # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
#
# i = 0
# seq = ['one', 'two', 'three']
# for element in seq:
#     print(i, seq[i])
#     i += 1
# # 0 one
# # 1 two
# # 2 three
#
# seq = ['one', 'two', 'three']
# for i, element in enumerate(seq):
#     print(i, element)
# # 0 one
# # 1 two
# # 2 three
# print(list(enumerate(seq)))
# # [(0, 'one'), (1, 'two'), (2, 'three')]


