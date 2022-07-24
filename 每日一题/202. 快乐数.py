# class Solution:
#     def isHappy(self, n):
#         if sum1 == 1:
#             return "true"
#         else:
#             n1 = sum(list(map(fun1, list(map(int, str(n))))))
#             return "false"


# x = n // 100  # -----求百位,除以100向上取整
# y = (n // 10) % 10  # 对10向上取整，再除以10的模
# z = n % 10  # -------求个位，除以10的模
# print("a的个位为：{}".format(z))
# print("a的十位为：{}".format(y))
# print("a的百位为：{}".format(x))

# # map
# def fun1(x, y):
#     return (x + y)
#
#
# print(list(map(fun1, [1], [2])))
# # 输出：[3]
# # 把参数1和2带入到fun1中去；
#
# print(list(map(fun1, [1, 3], [2, 5])))
# 输出：[3, 8]


# x = 199
# a, b, c = map(int, str(x))
# print(a, b, c)
# lis1 = list(map(int, str(x)))
# print(lis1)


# n2 = sum(list(map(fun1, list(map(int, str(n1))))))
# sum1 = 1


# # using recursion ————还没解决
# def factorial(n):
#     if n == 1:
#         return 'true'
#     else:
#         return factorial(sum(list(map(fun1, list(map(int, str(n)))))))
#
#
# try:
#     # using factorial:
#     def factorial(n):
#         if n == 1:
#             return 'true'
#         else:
#             return factorial(sum(list(map(fun1, list(map(int, str(n)))))))
# except RecursionError:
#     print("1")
#
# print(factorial(2))

# # using recursion
# def factorial(n):
#     mid = set()
#     if n == 1:
#         return True
#     if n in mid:
#         return False
#     else:
#         mid.add(n)
#         return factorial(sum(list(map(fun1, list(map(int, str(n)))))))
#
#
# print(factorial(2))

# # using recursion ————还没解决
# def fun1(x):
#     return x ** 2
#
#
# class Solution:
#     def isHappy(self, n):
#         mid = set()
#         if n == 1:
#             return True
#         if n in mid:
#             return False
#         else:
#             mid.add(n)
#             return self.isHappy(sum(list(map(fun1, list(map(int, str(n)))))))
#
#
# Soga = Solution()
# Answer = Soga.isHappy(25)
# print(Answer)

# n = 19
# sum1 = 0
# while n > 0:
#     bit = n % 10
#     sum1 += bit ** 2
#     n = n // 10
#
# print(sum1)

# n = 199
# lis = []
# while n > 0:
#     m = n % 10
#     n = n // 10
#     lis.append(m)
#
# print(lis)
# lis.reverse()
# print(lis)


# n = 19
# sum1 = 0
# while n > 0:
#     bit = n % 10
#     sum1 += bit ** 2
#     n = n // 10
#
# print(sum1)

# def SquareSum(n):
#     sum1 = 0
#     while n > 0:
#         bit = n % 10
#         sum1 += bit ** 2
#         n = n // 10
#     return sum1


# print(SquareSum(199))

# def fun1(x):
#     return x ** 2
#
#
# def SquareSum(num):
#     sum(list(map(fun1, list(map(int, str(num))))))


# class Solution:
#
#     # def SquareSum(self, n):
#     #
#     #     sum1 = 0
#     #     while n > 0:
#     #         bit = n % 10
#     #         sum1 += bit ** 2
#     #         n = n // 10
#     #     return sum1
#     def fun1(self, x):
#         return x ** 2
#
#
#     def SquareSum(self, num):
#         return sum(list(map(self.fun1, list(map(int, str(num))))))
#
#     def isHappy(self, n):
#         fast = slow = n
#         while True:
#             slow = self.SquareSum(slow)
#             fast = self.SquareSum(fast)
#             fast = self.SquareSum(fast)
#             # fast 总是比 slow跑得快，当比他快一轮时
#             if slow == fast:
#                 return slow == 1
#
#
# Soga = Solution()
# Answer = Soga.isHappy(19)
# print(Answer)

# 参考：https://leetcode.cn/problems/happy-number/solution/acm-xuan-shou-tu-jie-leetcode-kuai-le-sh-oj8g/
class Solution:

    # 求正整数 num 每个位置上数字的平方和

    def fun1(self, x):
        return x ** 2

    def getNext(self, num):
        # happy_sum = 0
        #
        # while num:
        #     happy_sum += (num % 10) ** 2
        #     num = num // 10
        #
        # return happy_sum
        return sum(list(map(self.fun1, list(map(int, str(num))))))

    def isHappy(self, n: int) -> bool:

        # 记录过程数据
        mid = set()

        while True:
            # 将当前数替换为它每个位置上的数字的平方和。
            n = self.getNext(n)
            # 如果为1，则是快乐数
            if n == 1:
                return True
            # 如果替换后的数再之前出现过，则说明陷入无限循环，此数不是快乐数
            if n in mid:
                return False
            else:
                mid.add(n)


Soga = Solution()
Answer = Soga.isHappy(25)
print(Answer)
