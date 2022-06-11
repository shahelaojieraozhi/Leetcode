# 力扣的官方答案
from collections import defaultdict
from collections import *

# class Solution:
#     def minWindow(self, s, t):
#         ans = float('inf')
#         i = start = end = 0
#         n = len(t)
#         need = Counter(t)
#
#         for j, c in enumerate(s, 1):
#             n -= need[c] > 0
#             need[c] -= 1
#             while not n:
#                 ans = min(ans, j - start)
#                 need[s[0]] += 1
#                 i += 1
#                 s = s[1:]
#
#                 start += 1
#                 while s[0] not in t:
#                     s = s[1:]
#                     start += 1
#                 n = 1
#
#
#         return "" if ans == float('inf') else s[start:len(s)]
#
#
# Soga = Solution()
# s = "ADOBECODEBANC"
# t = "ABC"
# Answer = Soga.minWindow(s, t)
# print(Answer)


from collections import Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         need, missing = Counter(t), len(t)
#         i = start = end = 0
#         for j, c in enumerate(s, 1):
#             missing -= need[c] > 0
#             need[c] -= 1
#             # if need[c] > 0:
#             #     missing -= need[c]
#             # need[c] -= 1
#
#             if not missing:
#                 while need[s[i]] < 0:
#                     need[s[i]] += 1
#                     i += 1
#                 if not end or j - i < end - start:
#                     start, end = i, j
#         return s[start:end]
#
#
# Soga = Solution()
# s = "ADOBECODEBANC"
# t = "ABC"
# Answer = Soga.minWindow(s, t)
# print(Answer)

from collections import defaultdict
from collections import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有t元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


Soga = Solution()
s = "ADOBECODEBANC"
t = "ABC"
Answer = Soga.minWindow(s, t)
print(Answer)
