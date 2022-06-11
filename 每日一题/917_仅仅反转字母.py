# 给你一个字符串 s ，根据下述规则反转字符串：
# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
# 返回反转后的 s 。

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # 先把给出来的字符翻转一下，并把非字母的字符去掉，形成新的数组
        lis = list(s)
        lis2 = list(s)
        lis2.reverse()
        lis3 = []
        for i in range(len(lis)):
            if lis2[i].isalpha() == True:
                lis3.append(lis2[i])
        # 新的数组一般比原数组短，要把新数组的元素填充到旧数组，而且还要有一定的条件
        # 于是想到了双指针法
        fast, slow = 0, 0
        while fast < len(lis):
            if lis[fast].isalpha() == True:
                lis[fast] = lis3[slow]
                slow += 1
            fast += 1
        return (''.join(lis))


Soga = Solution()
Answer = Soga.reverseOnlyLetters("a-bC-dEf-ghIj")
print(Answer)
