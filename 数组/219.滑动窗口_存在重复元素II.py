class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        for i, num in enumerate(nums):
            if len(window) == k + 1:
                left = nums[i - k - 1]
                window.remove(left)
            if num in window:
                return True
            window.add(num)
        return False


Soga = Solution()
nums = [1, 2, 3, 1, 2, 3]
Answer = Soga.containsNearbyDuplicate(nums, 2)
print(Answer)

# class Solution:
#     def containsNearbyDuplicate(self, nums, k):
#         window = set()
#         for i, num in enumerate(nums):
#             if len(window) == k + 1:
#                 window.remove(nums[i - 1 - k])
#             if num in window:
#                 return True
#             window.add(num)
#         return False
#
#
# Soga = Solution()
# nums = [1, 2, 3, 1, 2, 3]
# Answer = Soga.containsNearbyDuplicate(nums, 2)
# print(Answer)
