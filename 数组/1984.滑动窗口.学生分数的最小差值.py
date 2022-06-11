# class Solution:
#     def minimumDifference(self, nums, k):
#         nums.sort()
#         ans = nums[k - 1] - nums[0]
#         for i in range(len(nums) - k + 1):
#             ans = min(ans, nums[k - 1 + i] - nums[i])
#         return ans
#
#
# Soga = Solution()
# nums = [9, 4, 1, 7]
# Answer = Soga.minimumDifference(nums, 2)
# print(Answer)


class Solution:
    def minimumDifference(self, nums, k) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
        # 上面一句抵下面四句
        # ans = nums[k - 1] - nums[0]
        # for i in range(len(nums) - k + 1):
        #     ans = min(ans, nums[k - 1 + i] - nums[i])
        # return ans


Soga = Solution()
nums = [9, 4, 1, 7]
Answer = Soga.minimumDifference(nums, 2)
print(Answer)
