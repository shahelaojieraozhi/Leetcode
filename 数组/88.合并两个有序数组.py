# class Solution:
#     def merge(self, nums, target):
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             middle = (left + right) // 2
#             if target == nums[middle]:
#                 return middle
#             elif target < nums[middle]:
#                 right = middle - 1
#             else:
#                 left = middle + 1
#
#         return left  # 为什么时right + 1需要好好想想
#
#
# Soga = Solution()
# nums = [1, 3, 5, 7, 10]
# target = 6
# Answer = Soga.merge(nums, target)
# print(Answer)

# class Solution:
#     def merge(self, nums1, m, nums2, n) -> None:
#         """自己敲得"""
#         # nums1 = nums1 + nums2
#         # nums1.sort()
#         # nums1 = nums1[n:]
#         # return nums1
#
#         # 得熟悉列表
#         # nums1[m:] = nums2
#         # nums1.sort()
#         # return nums1
#
#         # 双指针
#         # num_sorted = []
#         fast = 0
#         for element in nums1:
#
#             if nums2[fast] >= element:
#                 nums1[fast] = element
#             else:
#                 nums1[fast] = nums2[fast]
#                 fast += 1
#
# Soga = Solution()
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# m = n = 3
# Answer = Soga.merge(nums1, m, nums2, n)
# print(Answer)

# 提交的时候记得改，nums1[:] = xx
# class Solution:
#     def merge(self, nums1, m, nums2, n) -> None:
#         # 双指针
#         num_sorted = []
#         P1 = P2 = 0
#         if m == 0:
#             return nums2
#         elif n == 0:
#             return nums1
#         else:
#
#             while P1 < m and P2 < n:
#                 # if (nums2[P2] >= nums1[P1]) and (nums1[P1] != 0):
#                 if nums2[P2] >= nums1[P1]:
#                     num_sorted.append(nums1[P1])
#                     P1 += 1
#                 else:
#                     num_sorted.append(nums2[P2])
#                     P2 += 1
#
#             # nums1 和 nums2 里面还有元素没传输
#             if len(num_sorted) < m + n:
#
#                 if P2 < n:
#                     # nums2 里面还剩一些元素
#                     num_sorted = num_sorted + nums2[P2:]
#
#                 else:
#
#                     # nums1 里面还剩一些元素
#                     for i in range(m + n - len(num_sorted)):
#                         num_sorted.append(nums1[P1 + i])
#
#             return num_sorted
#
#
# Soga = Solution()
# # nums1 = [-1, 0, 3, 0, 0, 0]  # [-1, 0, 0, 1, 2, 2, 3, 3, 3]
# # nums2 = [1, 2, 2, 6]
# # n = len(nums2)
# # m = len(nums1) - n
#
# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# n = len(nums2)
# m = len(nums1) - n
#
# Answer = Soga.merge(nums1, m, nums2, n)
# print(Answer)

"""https://leetcode.cn/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/"""


class Solution:
    def merge(self, nums1, m, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted

        return nums1


Soga = Solution()
nums1 = [-1, 0, 3, 0, 0, 0, 0]  # [-1, 0, 0, 1, 2, 2, 3, 3, 3]
nums2 = [1, 2, 2, 6]
n = len(nums2)
m = len(nums1) - n
Answer = Soga.merge(nums1, m, nums2, n)
print(Answer)

#  # 从屁股开始
'参考：https://leetcode.cn/problems/merge-sorted-array/solution/fu-xue-ming-zhu-dong-hua-ti-jie-cong-hou-teq6/'
# class Solution():
#     def merge(self, nums1, m, nums2, n):
#         k = m + n - 1
#         while m > 0 and n > 0:
#             if nums1[m - 1] > nums2[n - 1]:
#                 nums1[k] = nums1[m - 1]
#                 m -= 1
#             else:
#                 nums1[k] = nums2[n - 1]
#                 n -= 1
#             k -= 1
#         nums1[:n] = nums2[:n]
#
#         return nums1
#
#
# Soga = Solution()
# nums1 = [-1, 0, 3, 0, 0, 0, 0]  # [-1, 0, 0, 1, 2, 2, 3, 3, 3]
# nums2 = [1, 2, 2, 6]
# n = len(nums2)
# m = len(nums1) - n
#
# Answer = Soga.merge(nums1, m, nums2, n)
# print(Answer)
