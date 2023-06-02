'自己写的暴力解法'
from collections import Counter

# class Solution:
#     def checkIfExist(self, arr):
#
#         # 排除出现很多零
#         dir_ = Counter(arr)
#         if dir_[0] > 1:
#             return True
#
#         for element in arr:
#             if ((element / 2) in arr) and (element != 0):
#                 return True
#         return False
#
#
# Soga = Solution()
# arr = [0, 0]
# Answer = Soga.checkIfExist(arr)
# print(Answer)


'自己写的双指针'


class Solution:
    def checkIfExist(self, arr):
        slow = 0
        while slow < len(arr):
            for fast in range(len(arr)):
                if (arr[slow] == 2 * arr[fast]) and fast != slow:
                    return True

            slow += 1
        return False


Soga = Solution()
arr = [-2, 0, 10, -19, 4, 6, -8]
Answer = Soga.checkIfExist(arr)
print(Answer)
