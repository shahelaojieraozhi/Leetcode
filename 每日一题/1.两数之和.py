class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


Soga = Solution()
nums = [2, 7, 11, 15]
Answer = Soga.twoSum(nums, 9)
print(Answer)

# 哈希表
# class Solution:
#     def twoSum(self, nums, target: int):
#         hashtable = dict()
#         for i, num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target - num], i]
#             hashtable[nums[i]] = i
#         return []
#
#
# Soga = Solution()
# nums = [2, 7, 11, 15]
# Answer = Soga.twoSum(nums, 17)
# print(Answer)
