# 官方给的答案：https://leetcode.cn/problems/rank-transform-of-an-array/solution/shu-zu-xu-hao-zhuan-huan-by-leetcode-sol-8zlu/
# 排序 + 哈希表

class Solution:
    def arrayRankTransform(self, arr):
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[v] for v in arr]


Soga = Solution()
arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
Answer = Soga.arrayRankTransform(arr)
print(Answer)


class Solution:
    def arrayRankTransform(self, arr):
        map1 = sorted(set(arr))
        map2 = {}
        for idx, element in enumerate(map1, 1):
            map2[element] = idx

        return [map2[v] for v in arr]


Soga = Solution()
arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
Answer = Soga.arrayRankTransform(arr)
print(Answer)
