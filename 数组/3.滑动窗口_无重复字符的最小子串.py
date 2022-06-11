class Solution:
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        n = len(s)
        max_length = -1
        flag = 0    # 判断有没有重复的序列，没有的话直接输出子序列的长度
        while right < n:   # 窗口右指针的范围
            str1 = s[left:(right+1)]    # 子序列
            while finddif(str1) == False:   # 判断条件
                flag += 1
                left += 1  # 左指针右移，窗口缩小
                str1 = s[left:(right + 1)]
                max_length = max(len(str1), max_length)
            pro_len = max(len(str1), max_length)
            right += 1

        return n if flag == 0 else pro_len


# 重复否？
def finddif(s):
    set1 = set()
    for c in s:
        set1.add(c)
    return False if len(set1) < len(s) else True


Soga = Solution()
s = "abcabcbb"
Answer = Soga.lengthOfLongestSubstring(s)
print(Answer)


# # 重复否？
# def finddif(s):
#     set1 = set()
#     for c in s:
#         set1.add(c)
#     return False if len(set1) < len(s) else True
#
#
# s = 'ABCDD'
# print(finddif(s))

# # del版答案
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s:
#             return 0
#         max_len = 0  # 最大长度
#         tp = []  # 放字符串的一个队列
#         for a in s:
#             while a in tp:
#                 del tp[0]  # 删除队列左边第一个，直到没有重复的字符串
#             tp.append(a)
#             if len(tp) > max_len:
#                 max_len = len(tp)
#         return max_len
#
#
# Soga = Solution()
# s = "abcabcbb"
# Answer = Soga.lengthOfLongestSubstring(s)
# print(Answer)

#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            # 当出现重复的时候
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1

            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


Soga = Solution()
s = "abcabcbb"
Answer = Soga.lengthOfLongestSubstring(s)
print(Answer)
