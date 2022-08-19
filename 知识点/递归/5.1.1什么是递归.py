# # 数列求和
# def listsum(numlist):
#     if len(numlist) == 1:
#         return numlist[0]
#     else:
#         return numlist[0] + listsum(numlist[1:])
#
#
# numlist = [1, 2, 3, 4, 5]
# print(listsum(numlist))


# 转换任意进制
def toStr(n, base):
    converString = '0123456789ABCDEF'
    if n < base:
        return converString[n]
    else:
        return toStr(n // base, base) + converString[n % base]


print(toStr(769, 16))
