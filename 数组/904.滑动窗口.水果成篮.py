from collections import Counter

class Solution:
    def totalFruit(self, fruits):
        start = 0
        res = -1
        count = Counter()
        for j, c in enumerate(fruits):
            count[c] += 1
            while len(count) > 2:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0:
                    del count[fruits[start]]
                start += 1
            res = max(res, j - start + 1)
        return res


Soga = Solution()
fruits = [1, 1, 6, 5, 6, 6, 1, 1, 1, 1]
Answer = Soga.totalFruit(fruits)
print(Answer)

# 6 5 6 6 居然没有用了


# class Solution(object):
#     def totalFruit(self, tree):
#         ans = i = 0
#         count = Counter()
#         for j, x in enumerate(tree):
#             count[x] += 1
#             while len(count) >= 3:
#                 count[tree[i]] -= 1
#                 if count[tree[i]] == 0:
#                     del count[tree[i]]
#                 i += 1
#             ans = max(ans, j - i + 1)
#         return ans
#
#
# Soga = Solution()
# fruits = [1, 1, 6, 5, 6, 6, 1, 1, 1, 1]
# Answer = Soga.totalFruit(fruits)
# print(Answer)



