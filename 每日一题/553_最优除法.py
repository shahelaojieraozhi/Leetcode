# 忘记看输出是啥了，以为输出的是结果
# class Solution:
#     def optimalDivision(self, nums):
#         n = len(nums)
#         if n > 2:
#             sec = nums[1]
#             for i in range(2, n):
#                 sec = sec / nums[i]
#             answer = nums[0]/sec
#             return answer
#         elif n == 2:
#             return nums[1]/nums[0]
#         else:
#             return nums[0]



# # 官方答案
# class Solution:
#     def optimalDivision(self, nums):
#         if len(nums) == 1:
#             return str(nums[0])
#         if len(nums) == 2:
#             return str(nums[0]) + "/" + str(nums[1])
#         return str(nums[0]) + "/(" + "/".join(map(str, nums[1:])) + ")"
#
#
# Soga = Solution()
# nums = [1000, 100, 10, 2]
# Answer = Soga.optimalDivision(nums)
# print(Answer)


# 结合官方答案，修改了一下
class Solution:
    def optimalDivision(self, nums):
        n = len(nums)
        if n > 2:
            return str(nums[0]) + "/(" + "/".join(map(str, nums[1:])) + ")"
        elif n == 2:
            return str(nums[1]) + '/' + str(nums[0])
        else:
            return str(nums[0])


Soga = Solution()
nums = [1000, 100, 10, 2]
Answer = Soga.optimalDivision(nums)
print(Answer)
