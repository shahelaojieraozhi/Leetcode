# # 自己尝试双指针,基本结构了,但是满足不了特殊情况
# class Solution:
#     def firstUniqChar(self, s):
#         slow = 0
#         n = len(s)
#         s1 = set()
#         for i in range(n):
#             s1.add(s[i])
#         if len(s1) <= n/2:
#             return -1
#         else:
#             for fast in range(slow+1,n):
#                 if s[slow] == s[fast]:
#                     slow += 1
#             return slow
#
#
# s = "dddccdbba"
# Soga = Solution()
# Answer = Soga.firstUniqChar(s)
# print(Answer)


# 方法一：使用哈希表存储频数
import collections


class Solution:
    def firstUniqChar(self, s):
        frequence = collections.Counter(s)
        for j, c in enumerate(s):
            if frequence[c] == 1:
                return j
        return -1


s = "dddccdbba"
Soga = Solution()
Answer = Soga.firstUniqChar(s)
print(Answer)

# collections.Counter(s)

# # 方法二：使用哈希表存储索引
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         position = dict()
#         n = len(s)
#         for i, ch in enumerate(s):
#             if ch in position:
#                 position[ch] = -1
#             else:
#                 position[ch] = i
#         first = n
#         for pos in position.values():
#             if pos != -1 and pos < first:
#                 first = pos
#         if first == n:
#             first = -1
#         return first
#
#
# s = "dddccdbba"
# Soga = Solution()
# Answer = Soga.firstUniqChar(s)
# print(Answer)


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         position = dict()
#         q = collections.deque()
#         n = len(s)
#         for i, ch in enumerate(s):
#             if ch not in position:
#                 position[ch] = i
#                 q.append((s[i], i))
#             else:
#                 position[ch] = -1
#                 while q and position[q[0][0]] == -1:
#                     q.popleft()
#         return -1 if not q else q[0][1]
#
#
# s = "dddccdbba"
# Soga = Solution()
# Answer = Soga.firstUniqChar(s)
# print(Answer)
