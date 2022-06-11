# 27. 移除元素
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# 链接：https://leetcode-cn.com/problems/remove-element
#
# 输入：nums = [3,2,2,3], val = 3
# 输出：2, nums = [2,2]
# 你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。


# 输入：nums = [0,1,2,2,3,0,4,2], val = 2
# 输出：5, nums = [0,1,4,0,3]

# class Solution:
#     def removeElement(self, nums, val):
#         lis = []
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 lis.append(i)
#         len_new = len(nums) - len(lis)
#         for i in range(len(lis)):
#             nums[lis[i]] = -1000
#         nums.sort(reverse=True)
#         return len_new, nums
#
#
# Soga = Solution()
# nums = [3, 2, 2, 3]
# val = 3
# Answer = Soga.removeElement(nums, val)
# print(Answer)

# 某网友答案
# class Solution:
#     def removeElement(self, nums, val):
#         j = len(nums)
#         for i in range(j - 1, -1, -1):
#             if nums[i] == val:
#                 nums.pop(i)
#         return len(nums)
#
#
# Soga = Solution()
# nums = [3, 2, 2, 3]
# val = 3
# Answer = Soga.removeElement(nums, val)
# print(Answer)


# # 代码随想录
# class Solution:
#     """双指针法
#     时间复杂度：O(n)
#     空间复杂度：O(1)
#     """
#
#     @classmethod
#     def removeElement(cls, nums, val):
#         fast = slow = 0
#
#         while fast < len(nums):
#
#             if nums[fast] != val:
#                 nums[slow] = nums[fast]
#                 slow += 1
#
#             # 当 fast 指针遇到要删除的元素时停止赋值
#             # slow 指针停止移动, fast 指针继续前进
#             fast += 1
#         return slow
#
#
# Soga = Solution()
# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2
# Answer = Soga.removeElement(nums, val)
# print(Answer)
# print(nums)






