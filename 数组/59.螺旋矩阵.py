# class Solution:
#
#     def generateMatrix(self, n):
#         # 初始化要填充的正方形
#         matrix = [[0] * n for i in range(n)]    # [[]*4]
#
#         left, right, up, down = 0, n - 1, 0, n - 1
#         number = 1  # 要填充的数字
#
#         while left < right and up < down:
#
#             # 从左到右填充上边
#             for x in range(left, right):
#                 matrix[up][x] = number
#                 number += 1
#
#             # 从上到下填充右边
#             for y in range(up, down):
#                 matrix[y][right] = number
#                 number += 1
#
#             # 从右到左填充下边
#             for x in range(right, left, -1):
#                 matrix[down][x] = number
#                 number += 1
#
#             # 从下到上填充左边
#             for y in range(down, up, -1):
#                 matrix[y][left] = number
#                 number += 1
#
#             # 缩小要填充的范围
#             left += 1
#             right -= 1
#             up += 1
#             down -= 1
#
#         # 如果阶数为奇数，额外填充一次中心
#         if n % 2:
#             matrix[n // 2][n // 2] = number
#
#         return matrix
#
#
# Soga = Solution()
# Answer = Soga.generateMatrix(4)
# print(Answer)

# class Solution:
#     def generateMatrix(self, n: int) -> [[int]]:
#         l, r, t, b = 0, n - 1, 0, n - 1
#         mat = [[0 for _ in range(n)] for _ in range(n)]
#         num, tar = 1, n * n
#         while num <= tar:
#             for i in range(l, r + 1):  # left to right
#                 mat[t][i] = num
#                 num += 1
#             t += 1
#             for i in range(t, b + 1):  # top to bottom
#                 mat[i][r] = num
#                 num += 1
#             r -= 1
#             for i in range(r, l - 1, -1):  # right to left
#                 mat[b][i] = num
#                 num += 1
#             b -= 1
#             for i in range(b, t - 1, -1):  # bottom to top
#                 mat[i][l] = num
#                 num += 1
#             l += 1
#         return mat
#
#
# Soga = Solution()
# Answer = Soga.generateMatrix(4)
# print(Answer)

# https://leetcode-cn.com/problems/spiral-matrix-ii/solution/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/

class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        l, t, r, b = 0, 0, n - 1, n - 1
        num = 1
        while num <= n*n:
            for i in range(l, r+1):
                mat[l][i] = num
                num += 1
            l += 1
            for i in range(t+1, b+1):
                mat[i][b] = num
                num += 1
            t += 1
            for i in range(r-1, l-2, -1):
                mat[r][i] = num
                num += 1
            r -= 1
            for i in range(b-1, t-1, -1):
                mat[i][t-1] = num
                num += 1
            b -= 1
        return mat


Soga = Solution()
Answer = Soga.generateMatrix(4)
print(Answer)
