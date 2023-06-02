# -*- coding: utf-8 -*-
"""
@Project ：python_basic knowledge 
@Time    : 2023/6/2 11:23
@Author  : Rao Zhi
@File    : 268.丢失的数字.py
@email   : raozhi@mails.cust.edu.cn
@IDE     ：PyCharm 

"""


# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums_refer = [i for i in range(len(nums) + 1)]
#         for element in nums_refer:
#             if element in nums:
#                 continue
#             else:
#                 return element
#
#
# nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
#
# S = Solution()
# print(S.missingNumber(nums))


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_refer = [i for i in range(len(nums) + 1)]
        for key in set(nums_refer) - set(nums):
            return key


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

S = Solution()
print(S.missingNumber(nums))

""" 这个快很多,  还不知道怎么取set里的元素, 用 for 取太不文雅了 """

"""   数学解法 ------  求和再求差 """


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = n * (n + 1) / 2
        nums_sum = sum(nums)
        return int(total_sum - nums_sum)


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

S = Solution()
print(S.missingNumber(nums))
