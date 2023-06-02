# -*- coding: utf-8 -*-
"""
@Project ：python_basic knowledge 
@Time    : 2023/5/29 10:17
@Author  : Rao Zhi
@File    : 217.存在重复元素.py
@email   : raozhi@mails.cust.edu.cn
@IDE     ：PyCharm 

"""

""" 
给你一个整数数组 nums. 如果任一值在数组中出现 至少两次 
返回 true ; 如果数组中每个元素互不相同, 返回 false.
"""

'''暴力解法, 直接报：超过时间限制'''

# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#
#         for i in nums:
#             same_point = 0
#             for j in nums:
#                 if i == j:
#                     same_point += 1
#                     if same_point > 1:
#                         return True
#
#         return False
#
#
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# # nums = [1, 2, 3, 4]
#
# S = Solution()
# print(S.containsDuplicate(nums))


''' 双指针也超时 '''
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#
#         for slow in range(len(nums)):
#             for fast in range(slow + 1, len(nums)):
#                 if nums[fast] != nums[slow]:
#                     fast += 1
#                 else:
#                     return True
#             slow += 1
#         return False
#
#
# # nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# # nums = [1, 2, 3, 4]
# nums = [1, 2, 3, 10, 6, 7, 8]
#
# S = Solution()
# print(S.containsDuplicate(nums))


""" 排序法 """


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        new_nums = sorted(nums)
        for i in range(1, len(new_nums)):
            if new_nums[i - 1] == new_nums[i]:
                return True
        return False


# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# nums = [1, 2, 3, 4]
nums = [1, 2, 3, 10, 6, 8, 8]

S = Solution()
print(S.containsDuplicate(nums))

"""  #######   note   ######  """
"""  
双指针的时间复杂度为 O(n)  而排序是 O(n * log n) 但是为什么双指针能爆？
应该是排序可以帧对这题的实际场景, 可能重复的数较小,在前面。而重复的数的索引值很大，因此即使是双指针也爆了

所以复杂度只是参考，实际应用要看情况
"""
