# 超时了
class Solution:
    def findMaxAverage(self, nums, k):
        ls = []
        res = sum(nums[:k])
        for i in nums:
            ls.append(i)
            while len(ls) == k:
                avg = float(sum(ls) / k)
                res = max(res, avg)
                ls.remove(ls[0])
        return float(res)


Soga = Solution()
nums = [1, 12, -5, -6, 50, 3]
target = 4
Answer = Soga.findMaxAverage(nums, target)
print(Answer)


# # 力扣官方答案
# class Solution:
#     def findMaxAverage(self, nums, k: int) -> float:
#         maxTotal = total = sum(nums[:k])
#         n = len(nums)
#
#         for i in range(k, n):
#             total = total + nums[i] - nums[i - k]  # (1+12-5-6) + 50 - 1
#             maxTotal = max(maxTotal, total)
#
#         return maxTotal / k
#
#
# Soga = Solution()
# nums = [1, 12, -5, -6, 50, 3]
# target = 4
# Answer = Soga.findMaxAverage(nums, target)
# print(Answer)
