class Solution:
    def shuffle(self, nums, n):
        res = [0 for _ in range(2 * n)]
        for i in range(n):
            res[2 * i] = nums[i]
            res[2 * i + 1] = nums[n + i]
        return res


S = Solution()
re = S.shuffle([5, 4, 1, 2, 6, 7], 3)
print(re)
