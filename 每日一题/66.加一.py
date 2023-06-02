'把列表转成整数的思路'


# class Solution:
#     # def plusOne(self, digits):
#     #     # 先转成整数
#     #     str1 = []
#     #     for element in digits:
#     #         str1 += str(element)
#     #     num = int(''.join(str1))
#     #
#     #     # num + 1
#     #     num += 1
#     #
#     #     # 再转换成列表
#     #     lis = []
#     #     num_lis = list(str(num))
#     #     for element in num_lis:
#     #         lis.append(int(element))
#     #
#     #     return lis
#
#     # 成熟版
#     def plusOne(self, digits):
#         digits = [str(a) for a in digits]
#         digits = str(int(''.join(digits)) + 1)
#         digits = [int(a) for a in digits]
#         return digits
#
#
# Soga = Solution()
# digits = [8, 9, 9]
# Answer = Soga.plusOne(digits)
# print(Answer)

'把列表的进位'


# class Solution:
#
#     def plusOne(self, digits):
#         # 量级不变的情况
#         p = 0
#         for element in digits[::-1]:
#             if element == 9:
#                 p += 1
#             else:
#                 break
#         digits[len(digits) - p - 1] += 1
#         digits[(len(digits) - p):] = [0 for i in range(p)]
#
#         # 量级发生改变
#         if digits[0] == 0:
#             # digits.insert(0, 1)
#             digits = [1] + digits
#         return digits
#
#
# Soga = Solution()
# digits = [9, 9, 9]
# # digits = [5, 1, 9, 9]
# Answer = Soga.plusOne(digits)
# print(Answer)


class Solution:

    def plusOne(self, digits):
        # 量级不变的情况
        p = 0
        for element in digits[::-1]:
            if element == 9:
                p += 1
            else:
                break
        digits[len(digits) - p - 1] += 1
        digits[(len(digits) - p):] = [0 for i in range(p)]

        # 量级发生改变
        if digits[0] == 0:
            # digits.insert(0, 1)
            digits = [1] + digits
        return digits


Soga = Solution()
digits = [9, 9, 9]
# digits = [5, 1, 9, 9]
Answer = Soga.plusOne(digits)
print(Answer)