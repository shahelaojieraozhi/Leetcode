import re
from collections import Counter

# cnt = Counter()
# for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#     cnt[word] += 1
# print(cnt)
# # Counter({'blue': 3, 'red': 2, 'green': 1})
#
# # words = re.findall(r'\w+', open('hamlet.txt').read().lower())
# # Counter(words).most_common(10)
#
# print(Counter('abracadabra').most_common(3))
# # [('a', 5), ('b', 2), ('r', 2)]

# c = Counter(a=3, b=1)
# d = Counter(a=1, b=2)
# print(c + d)  # Counter({'a': 4, 'b': 3})
# print(c & d)  # Counter({'a': 1, 'b': 1})
# print(c | d)  # Counter({'a': 3, 'b': 2})
#
# 统计词频
# colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# result = {}
# for color in colors:
#     if result.get(color) == None:
#         result[color] = 1
#     else:
#         result[color] += 1
# print(result)   # {'red': 2, 'blue': 3, 'green': 1}


# colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# c = Counter(colors)
# print(dict(c))  # {'red': 2, 'blue': 3, 'green': 1}

# # 判断是否包含某元素
# c = Counter(['eggs', 'ham'])
# print(c['bacon'])  # 不存在就返回0
# # 0

# # 删除元素：
# c = Counter(['sausage', 'zhi', 'yue'])
# c['sausage'] = 0                        # counter entry with a zero count
# print(c)  # Counter({'zhi': 1, 'yue': 1, 'sausage': 0})
# del c['sausage']
# print(c)  # Counter({'zhi': 1, 'yue': 1})

# # 获得所有元素：
# c = Counter(a=4, b=2, c=0, d=-2)
# print(list(c.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b']

# # 查看最常见出现的k个元素：
# print(Counter('abracadabra').most_common(3))  # [('a', 5), ('r', 2), ('b', 2)]

# # Counter更新：
# c = Counter(a=3, b=1)
# d = Counter(a=1, b=2)
# print(c + d)  # 相加
# # Counter({'a': 4, 'b': 3})
# print(c - d)  # 相减，如果小于等于0，删去
# # Counter({'a': 2})
# print(c & d)  # 求最小
# # Counter({'a': 1, 'b': 1})
# print(c | d)  # 求最大
# # Counter({'a': 3, 'b': 2})

# # subtract
# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# c.subtract(d)
# print(c)
# # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

# # 实例应用：
# from collections import Counter
#
# lines = open("./Counter_ex.txt", "r").read().splitlines()
# lines = [lines[i].split(" ") for i in range(len(lines))]
# words = []
# for line in lines:
#     words.extend(line)
# result = Counter(words)
# print(result.most_common(10))  # [('i', 5), ('dad', 3), ('dw', 3), ('hw', 3), ('hdwh', 1), ('he', 1), ('ded', 1)]

# from collections import Counter
#
# result = Counter()
# with open("./data/input.txt", "r") as f:
#     while True:
#         lines = f.read(1024).splitlines()
#         if lines == []:
#             break
#         lines = [lines[i].split(" ") for i in range(len(lines))]
#         words = []
#         for line in lines:
#             words.extend(line)
#         tmp = Counter(words)
#         result += tmp
#
# print(result.most_common(10))

# #
# A = [1, 2, 3]
# B = [['a', 'b']]
# A.extend([4])
# print(A)    # [1, 2, 3, 4]
#
# A = [1, 2, 3]
# B = [['a', 'b']]
# A.append(4)
# print(A)    # [1, 2, 3, 4]


# # extend() 函数的功能:
# # 用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# A = [1, 2, 3]
# B = [['a', 'b']]
# A.extend([4])
# A.extend([5, 6])
# B.extend(['c', 'd'])
# B.extend([['e', 'f']])
# print(A)    # [1, 2, 3, 4, 5, 6]
# print(B)    # [['a', 'b'], 'c', 'd', ['e', 'f']]

# extend() 函数、append()函数、+ 与 += 功能比较:

# A = [1, 2, 3]
# B = [4, 5, 6]
# print(A.append(B))
# print(A)

# A = [1, 2, 3]
# B = [4, 5, 6]
# print(A.extend(B))  # None
# print(A)    # [1, 2, 3, 4, 5, 6]

# A = [1, 2, 3]
# B = [4, 5, 6]
# print(A+B)  # [1, 2, 3, 4, 5, 6]
# print(A)    # [1, 2, 3]

# A = [1, 2, 3]
# B = [4, 5, 6]
# A += B
# print(A)    # [1, 2, 3, 4, 5, 6]

# str = "the different about split and splitlines is ..."
# # 默认是None(以空白字符串为分隔符)
# print(str.split())  # ['the', 'different', 'about', 'split', 'and', 'splitlines', 'is', '...']
# # 以i 为分隔符
# print(str.split('i'))   # ['the d', 'fferent about spl', 't and spl', 'tl', 'nes ', 's ...']
# # 以第一个i分隔
# print(str.split('i', 1))  # ['the d', 'fferent about split and splitlines is ...']


# u = "www.jeapedu.com\nwww.chinagame.me\nwww.quanzhan.org"
# print(u.splitlines())  # ['www.jeapedu.com', 'www.chinagame.me', 'www.quanzhan.org']
# # split('\n')效果一样
# print(u.split("\n"))  # ['www.jeapedu.com', 'www.chinagame.me', 'www.quanzhan.org']

# # 但是下面的测试用例就必须用splitlines了
# t = """www.jeapedu.com
#        www.chinagame.me
#        www.quanzhan.org
#      """
# print(t.splitlines())
# print(t)

# t = """www.jeapedu.com
# www.chinagame.me
# www.quanzhan.org"""
# print(t.splitlines())   # ['www.jeapedu.com', 'www.chinagame.me', 'www.quanzhan.org']

# #
# a = ' abc de a  1  '
# b = a.strip()
# print(b)    # abc de a  1
# print(a.lstrip())   # abc de a  1
# print(a.rstrip())   #  abc de a  1

# 三个函数都可以传入一个参数(这里以'do'为例)，指定要去除的首尾字符，编译器会去除两端所有相应的字符，直到没有匹配的字符。
# 指定的字符表示的一种组合，例如'do'表示'dd','do','od','oo','ddd','ooo'等

# dodo = "say hello say boy saaayaaas"
# print(dodo.strip('say'))  # hello say boy
# print(dodo.strip('yas'))  # hello say boy
# # 当传入的参数中加入空格时
# print(dodo.strip('say '))
#
# print(dodo.lstrip('say'))
# print(dodo.rstrip('say'))
