# 977. 有序数组的平方
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# import time
#
#
# class Solution:
#     def sortedSquares(self, nums):
#         start = time.time()
#         for i in range(len(nums)):
#             nums[i] = nums[i] * nums[i]
#         nums.sort()
#         end = time.time()
#         return nums, end - start
#
#
# Soga = Solution()
# nums = [-4, -1, 0, 3, 10]
# Answer, time_use = Soga.sortedSquares(nums)
# print(Answer)
# print("程序需要：%10.7f seconds" % time_use)


# # 双指针
# class Solution:
#     def sortedSquares(self, nums):
#         if len(nums) == 1:
#             return [nums[0] * nums[0]]
#
#         # 初始化双指针
#         left = 0
#         right = len(nums) - 1
#
#         # 存储结果数组，从数组末尾开始存储
#         res = [-1] * len(nums)
#         # nums = [-4, -1, 0, 3, 10] res = [-1, -1, -1, -1, -1]
#
#         site = len(nums) - 1
#
#         # 注意这里是 <=
#         while left <= right:
#             # 从两端遍历，将平方数组大得存储在 res 数组中
#             if nums[left] * nums[left] < nums[right] * nums[right]:
#                 res[site] = nums[right] * nums[right]
#                 right -= 1
#             else:
#                 res[site] = nums[left] * nums[left]
#                 left += 1
#
#             site -= 1
#
#         return res
#
#
# Soga = Solution()
# nums = [-4, -1, 0, 3, 10]
# Answer = Soga.sortedSquares(nums)
# print(Answer)

# https://leetcode-cn.com/problems/squares-of-a-sorted-array/solution/acm-xuan-shou-tu-jie-leetcode-you-xu-shu-h8le/


# # 自己写的
# class Solution:
#     def sortedSquares(self, nums):
#         i, j = 0, len(nums) - 1
#         result = list([0] * (j + 1))
#         k = j
#         while k + 1:
#             if nums[j] * nums[j] > nums[i] * nums[i]:
#                 result[k] = nums[j] * nums[j]
#                 j -= 1
#             else:
#                 result[k] = nums[i] * nums[i]
#                 i += 1
#             k -= 1
#         return result
#
#
# Soga = Solution()
# nums = [-7, -3, 2, 3, 11]
# Answer = Soga.sortedSquares(nums)
# print(Answer)

class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        fast = slow = 0
        for i in range(len(nums)):
            if nums[fast] <= nums[slow]:
                nums[slow] = nums[fast]
                slow +=1
                # 当 fast 指针遇到要删除的元素时停止赋值
                # slow 指针停止移动, fast 指针继续前进
            fast += 1
            return nums


Soga = Solution()
nums = [-4, -1, 0, 3, 10]
Answer = Soga.sortedSquares(nums)
print(Answer)
