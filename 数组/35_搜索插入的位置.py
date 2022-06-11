# # 35. 搜索插入位置：
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
# 链接：https://leetcode-cn.com/problems/search-insert-position

# 代码随想录里的答案
# class Solution:
#     def searchInsert(self, nums, target):
#         left, right = 0, len(nums) - 1
#         while right >= left:
#             middle = (left + right) // 2
#             if nums[middle] > target:
#                 left = middle + 1
#             elif nums[middle] < target:
#                 right = middle - 1
#             else:
#                 return(middle)
#             return(right + 1)


# # 自己写的，我觉得偏底层
# class Solution:
#     def searchInsert(self, nums, target):
#         L = len(nums) - 1
#         if target in nums:
#             if L == 0:
#                 return 0
#             else:
#                 while L:
#                     if target == nums[L]:
#                         return L
#                     L -= 1
#                     if L == 0:
#                         return 0
#         else:
#             nums.append(target)
#             nums.sort()
#             return nums.index(target)
#
#
# Soga = Solution()
# nums = [1, 3, 5, 6]
# target = 5
# Answer = Soga.searchInsert(nums, target)
# print(Answer)

# # 评论区答案
# class Solution:
#     def searchInsert(self, nums, target):
#         if target in nums:
#             return nums.index(target)
#         else:
#             nums.append(target)
#             nums.sort()
#             return nums.index(target)

# # 二分法：
# class Solution:
#     def search(self, nums, target):
#         left, right = 0, len(nums) - 1
#
#         while left <= right:
#             middle = (left + right) // 2
#             if target < nums[middle]:
#                 right = middle - 1
#             elif target > nums[middle]:
#                 left = middle + 1
#             else:
#                 return middle
#         return right + 1        # 为什么时right + 1需要好好想想
#
#
# Soga = Solution()
# nums = [1, 3, 5, 6]
# target = 0
# Answer = Soga.search(nums, target)
# print(Answer)


class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return left        # 为什么时right + 1需要好好想想


Soga = Solution()
nums = [1, 3, 5, 7, 10]
target = 6
Answer = Soga.search(nums, target)
print(Answer)

# 复杂度分析:
# 时间复杂度：O(\log n)O(logn)，其中 nn 为数组的长度。二分查找所需的时间复杂度为 O(\log n)O(logn)。
# 空间复杂度：O(1)O(1)。我们只需要常数空间存放若干变量。
