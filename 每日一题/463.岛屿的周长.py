# # # By myself
# class Solution:
#     def islandPerimeter(self, grid):
#         die = 0     # 记重叠的边个数
#         counter = 0     # 记grid中出现 1 的个数
#         m, n = len(grid), len(grid[0])  # 获得grid的规格
#
#         for k in range(m):  # m = 4; n = 4
#             # 先在4*4 左右两边各添加两个零，相当于加了8个零，左右各四个零围着
#             grid[k].insert(n, 0)
#             grid[k].insert(0, 0)
#         # 上下各加6个零围起来
#         grid.insert(m, [0] * (n + 2))
#         grid.insert(0, [0] * (n + 2))
#         # 生成了一个 6 * 6 的矩阵了
#
#         for i in range(m + 2):
#             for j in range(n + 2):
#                 if grid[i][j]:
#                     counter += 1
#                     if grid[i - 1][j]:  # 上
#                         die += 1
#                     if grid[i + 1][j]:  # 下
#                         die += 1
#                     if grid[i][j - 1]:  # 左
#                         die += 1
#                     if grid[i][j + 1]:  # 右
#                         die += 1
#         return counter * 4 - die
#
#
# S = Solution()
# # grid = [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
# grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# print(S.islandPerimeter(grid))


# class Solution:
#     def islandPerimeter(self, grid) -> int:
#         m, n = len(grid), len(grid[0])
#         ans = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]:
#                     if (i + 1 < m and not grid[i + 1][j]) or i == m - 1:
#                         ans += 1
#                     if (i - 1 >= 0 and not grid[i - 1][j]) or i == 0:
#                         ans += 1
#                     if (j + 1 < n and not grid[i][j + 1]) or j == n - 1:
#                         ans += 1
#                     if (j - 1 >= 0 and not grid[i][j - 1]) or j == 0:
#                         ans += 1
#         return ans


# class Solution {
#     public int islandPerimeter(int[][] grid) {
#         int total = 0;
#         // 重合边长总和
#         int innerTotal = 0;
#         for (int i = 0; i < grid.length; i++) {
#             int[] temp = grid[i];
#             for (int j = 0; j < temp.length; j++) {
#                 if (grid[i][j] == 1) {
#                     total += 4;
#                 } else {
#                     continue;
#                 }
#                 // 左边有格子
#                 if (j > 0 && grid[i][j - 1] == 1) {
#                     innerTotal++;
#                 }
#                 // 右边有格子
#                 if (j < temp.length - 1 && grid[i][j + 1] == 1) {
#                     innerTotal++;
#                 }
#                 // 上边有格子
#                 if (i > 0 && grid[i - 1][j] == 1) {
#                     innerTotal++;
#                 }
#                 // 下边有格子
#                 if (i < grid.length - 1 && grid[i + 1][j] == 1) {
#                     innerTotal++;
#                 }
#             }
#         }
#
#         return total - innerTotal;
#     }
# }

# 类似虚拟头结点解法

def islandPerimeter(grid) -> int:
    c = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):  # m = 4; n = 4
        # 先在4*4 左右两边各添加两个零，相当于加了8个零，左右各四个零围着
        grid[i].insert(n, 0)
        grid[i].insert(0, 0)
    # 上下各加6个零围起来
    grid.insert(m, [0] * (n + 2))
    grid.insert(0, [0] * (n + 2))
    # 生成了一个 6 * 6 的矩阵了

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if grid[i][j] == 1:
                c += [grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i][j + 1]].count(0)
                # 1 上下左右有几个0就有几条边
    return c


if __name__ == '__main__':
    grid = [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
    # grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(islandPerimeter(grid))

