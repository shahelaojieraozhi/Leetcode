# for i in range(1, 1):
#     print(i)
#     print('1')
# print(1)

# import numpy as np
# grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# arr = np.array(grid)
# print(arr.shape)


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]


m, n = len(grid), len(grid[0])  # m = 4; n = 4
for i in range(m):
    grid[i].insert(n, 0)
    grid[i].insert(0, 0)
# grid.insert(m, [0] * (n + 2))
# grid.insert(0, [0] * (n + 2))

print(grid)