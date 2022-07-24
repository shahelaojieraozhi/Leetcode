import numpy as np

x = np.arange(4).reshape((2, 2))
print(x)
print(x.transpose())
print(x)

print(x.transpose((0, 1)))
# [[0 1]
#  [2 3]]
print(x.transpose((1, 0)))
# [[0 2]
#  [1 3]]


# x = np.arange(12).reshape((2, 3, 2))
# print(x)
#
# x.transpose((1, 0, 2))
# print(x)


# import numpy as np
#
# # A是array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
# A = np.arange(16)
#
# # 将A变换为三维矩阵
# A = A.reshape(2,2,4)
# print(A)
