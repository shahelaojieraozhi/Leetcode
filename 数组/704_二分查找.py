# 704. 二分查找
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target，
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1

# # 自己先练的
# class Solution:
#     def search(self, nums, target):
#         L = len(nums)
#         while L:
#             if nums[L - 1] == target:
#                 return L - 1
#             L -= 1
#             if L == 0:
#                 return -1
#
#
# Soga = Solution()
# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
# Answer = Soga.search(nums, target)
# print(Answer)

# 二分法：
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:   # 找在前半段还是后半段
                left = middle + 1
            elif nums[middle] > target:     # 找在前半段还是后半段
                right = middle - 1
            else:
                return middle
        return -1


Soga = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
Answer = Soga.search(nums, target)
print(Answer)
