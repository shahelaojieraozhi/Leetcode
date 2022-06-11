# num1 = "1+1i"
# num2 = "1+1i"
# real1 = list(num1.split('+'))
# real1, imag1 = num1[:-1].split('+')
# real2 = int(real1)
# print(real1, imag1)

# class Solution:
#     def complexNumberMultiply(self, num1: str, num2: str) -> str:
#         real1, imag1 = map(int, num1[:-1].split('+'))
#         real2, imag2 = map(int, num2[:-1].split('+'))
#         sum_real = real1 * real2 - imag2 * imag1
#         sum_imag = imag1 * real2 + real1 * imag2
#         ret = ('%d+%di' % (sum_real, sum_imag))
#         return ret
#
#
# Soga = Solution()
# num1 = "1+1i"
# num2 = "1+1i"
# Answer = Soga.complexNumberMultiply(num1, num2)
# print(Answer)

# 官方解题
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return f'{real1 * real2 - imag1 * imag2}+{real1 * imag2 + imag1 * real2}i'
