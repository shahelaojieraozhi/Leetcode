class Solution:
    def maximumDifference(self, nums):
        n = len(nums)
        lis = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    lis.append(nums[j] - nums[i])
        if lis==[]:
            return -1
        else:
            return max(lis)


Soga = Solution()
nums = [1, 2]
Answer = Soga.maximumDifference(nums)
print(Answer)

