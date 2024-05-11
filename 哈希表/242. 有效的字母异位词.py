# -*- coding: utf-8 -*-
"""
@Project ：python_basic knowledge 
@Time    : 2023/9/6 7:56
@Author  : Rao Zhi
@File    : 242. 有效的字母异位词.py
@email   : raozhi@mails.cust.edu.cn
@IDE     ：PyCharm 

"""


class Solution:
    """很好的错误范例"""

    def isAnagram(self, s: str, t: str) -> bool:
        for element in s:
            if element in t:
                s.replace(element, '')
                t.replace(element, '')
                if len(s) == len(t):
                    continue
                else:
                    return False
            else:
                return False
        return True


# Soga = Solution()
# # s = "anagram"
# # t = "nagaram"
# # s = "rat"
# # t = "car"
#
# s = "aacc"
# t = "ccac"
#
#
# # s = "aa"
# # t = "a"
#
# Answer = Soga.isAnagram(s, t)
# print(Answer)

# class Solution:
#
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_dict = {}
#         t_dict = {}
#
#         for element in s:
#             if element in s_dict:
#                 s_dict[element] += 1
#             else:
#                 s_dict[element] = 0
#                 s_dict[element] += 1
#
#         for element in t:
#             if element in t_dict:
#                 t_dict[element] += 1
#             else:
#                 t_dict[element] = 0
#                 t_dict[element] += 1
#
#         if s_dict == t_dict:
#             return True
#         else:
#             return False
#
#
# Soga = Solution()
#
# # s = "rat"
# # t = "car"
#
# s = "aa"
# t = "a"
#
# # s = "anagram"
# # t = "nagaram"
# Answer = Soga.isAnagram(s, t)
# print(Answer)

# # coding = utf-8
# d = {"name": "Alex", "age": 26, "hobbie": "大保健"}
# l = ["Rebeeca", "Katrina", "Rachel"]
#
#
# def change_data(info, girls):
#     info["hobbie"] = "学习"
#     girls.append("XiaoYun")
#
#
# change_data(d, l)
# print(d, l)
