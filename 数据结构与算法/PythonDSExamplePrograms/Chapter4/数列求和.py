
# 问题:给定一个列表,返回所有数的和
def listsum(numlist):
    Sum = 0
    for i in numlist:
        Sum += i
    return Sum


print(listsum([1, 3, 5, 6]))
