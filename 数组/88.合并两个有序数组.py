

class Solution:
    def merge(self, nums, target):
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
Answer = Soga.merge(nums, target)
print(Answer)


