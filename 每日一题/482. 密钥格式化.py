# -*- coding: utf-8 -*-
"""
@Project :python_basic knowledge 
@Time    : 2024/6/4 11:17
@Author  : Rao Zhi
@File    : 482. 密钥格式化.py
@email   : raozhi@mails.cust.edu.cn
@IDE     : PyCharm 
@描述    :
@detail  :
@infer   :
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_s = "".join(s.split("-")).upper()[::-1]
        res = ""
        for ele in range(len(new_s) // k):
            res += new_s[ele * k:(ele + 1) * k] + "-"
        if len(new_s) % k != 0:
            res += new_s[-(len(new_s) % k):] + "-"
        res = res[::-1]
        return res[1:]

        # res = ""
        # restr = ""
        # for idx, sub_str in enumerate(new_S):
        #     if idx == 0:
        #         res += sub_str.upper() + "-"
        #     else:
        #         if len(sub_str) < k:
        #             restr += sub_str.upper()
        #         else:
        #             res += sub_str.upper() + "-"
        # res += restr
        # return res


slu = Solution()
S = "5F3Z-2e-9-w"
# S = "2-4A0r7-4k"
k = 4
print(slu.licenseKeyFormatting(S, k))
