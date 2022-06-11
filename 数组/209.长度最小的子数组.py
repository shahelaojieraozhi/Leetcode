# class Solution:
#     def minSubArrayLen(self, target, nums):

# # 代码随想录
# class Solution:
#     """双指针法
#     时间复杂度：O(n)
#     空间复杂度：O(1)
#     """
#
#     @classmethod
#     def minSubArrayLen(cls, nums, target):
#         fast = slow = 0
#         result = []
#         for i in range(10):
#             result.append([])
#         temp = []
#         while fast < len(nums):
#             result[slow].append(nums[fast])
#             if sum(result[slow]) < target:
#                 fast += 1
#             else:
#                 fast = slow
#                 temp.append(result[slow])
#                 slow += 1
#         if sum(result[0]) < target:
#             return 0
#         else:
#             L = []
#             for i in range(len(temp)):
#                 L.append(len(temp[i]))
#             lis_min = min(L)
#             return lis_min
#
#
# Soga = Solution()
# target = 7
# nums = [2, 3, 1, 2, 4, 3]
# Answer = Soga.minSubArrayLen(nums, target)
# print(Answer)
# print(nums)

# # 暴力求解：（by myself）
# class Solution:
#     def minSubArrayLen(self, s, nums):
#         n = len(nums)
#         sum2 = 0
#         lis = []
#         if max(nums) >= s:
#             return 1
#         if sum(nums) < s:
#             return 0
#         else:
#             for i in range(n):
#                 sum2 = nums[i]
#                 for j in range(i + 1, n):
#                     sum2 = sum2 + nums[j]
#                     if sum2 >= s:
#                         lis.append(j - i + 1)
#                         break
#             return min(lis)
#
#
# Soga = Solution()
# s = 15
# nums = [1, 2, 3, 4, 5]
# Answer = Soga.minSubArrayLen(s, nums)
# print(Answer)

# # 代码随想录
# class Solution:
#     def minSubArrayLen(self, s, nums):
#         # 定义一个无限大的数
#         res = float("inf")  # res是长度最小的子数组
#         Sum = 0
#         index = 0  # 起始位置索引
#         for i in range(len(nums)):
#             Sum += nums[i]
#             while Sum >= s:
#                 res = min(res, i - index + 1)  # res = 结束位置索引 减去 起始位置+1
#                 Sum -= nums[index]  # 向后移动一格
#                 index += 1  # 起始位置加一
#         return 0 if res == float("inf") else res
#
#
# Soga = Solution()
# s = 7
# nums = [2, 3, 1, 2, 4, 3]
# Answer = Soga.minSubArrayLen(s, nums)
# print(Answer)
# print(nums)


# class Solution:
#     def minSubArrayLen(self, s, nums):
#         if max(nums) >= s:
#             return 1
#         if sum(nums) < s:
#             return 0
#         else:
#             index = 0
#             sum1 = 0
#             res = float("inf")
#             for i in range(index, len(nums)):
#                 sum1 += nums[i]
#                 while sum1 >= s:
#                     res = min(res, i - index + 1)
#                     sum1 -= nums[index]
#                     index += 1
#         return res
#
#
# Soga = Solution()
# s = 11
# nums = [1, 2, 3, 4, 5]
# Answer = Soga.minSubArrayLen(s, nums)
# print(Answer)
# print(nums)

# 结构有问题，还没解决
#                 while sum1 >= s:
#                     length.append(len(ls))
#                     front += 1
#                     ls = []
#                     break


# 力扣的官方答案
class Solution:
    def minSubArrayLen(self, s, nums):
        sum = 0
        ans = float('inf')
        start, end = 0, 0
        n = len(nums)
        for end in range(n):
            sum += nums[end]
            while sum >= s:
                ans = min(ans, end - start + 1)
                sum -= nums[start]
                start += 1
        return 0 if ans == float('inf') else ans


Soga = Solution()
s = 11
nums = [1, 2, 3, 4, 5]
Answer = Soga.minSubArrayLen(s, nums)
print(Answer)
print(nums)
