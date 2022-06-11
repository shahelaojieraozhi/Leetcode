# 给定一个 n*n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        l, t, r, b = 0, 0, n - 1, n - 1
        num = 1
        while num <= n * n:
            for i in range(l, r + 1):
                matrix[l][i] = num
                num += 1
            l += 1
            for i in range(t + 1, b + 1):
                matrix[i][b] = num
                num += 1
            t += 1
            for i in range(r - 1, l - 2, -1):
                matrix[r][i] = num
                num += 1
            r -= 1
            for i in range(b - 1, t - 1, -1):
                matrix[i][t - 1] = num
                num += 1
            b -= 1
        return matrix


Soga = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Answer = Soga.rotate(matrix)
print(Answer)
