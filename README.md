# Leetcode

My way to make my coding ability more strong







# python全局变量

参考:[Python 如何在局部修改全局变量 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/103906261)

**字符串**

```python3
# coding = utf-8
name = 'Jack'
def rename():
    global name #在函数内部声明全局变量，只有特殊情况下使用
    name = 'Pydjon'
    print(name)
rename()
print(name)
```

输出:

```
'Pydjon'
```

**传递列表、字典、集合产生的现象**

```python3
# coding = utf-8
d = {"name":"Alex","age":26,"hobbie":"大保健"}
l = ["Rebeeca","Katrina","Rachel"]

def change_data(info,girls):

    info["hobbie"] = "学习"
    girls.append("XiaoYun")

change_data(d,l)
print(d,l)
```

输出：

```
执行结果{‘name’: ‘Alex’, ‘age’: 26, ‘hobbie’: ‘学习’} [‘Rebeeca’, ‘Katrina’, ‘Rachel’, ‘XiaoYun’]
```

不是说不能在函数里改全局变量么，怎么改了呀？

![](E:\code\python_code\python_basic knowledge\Q_bin\Leetcode_刷题\images\v2-e004ede5ffabe982614fa6e3507cfcd5_r.jpg)

​		根据上图我们能看出， 程序只是把d这个dict的内存地址传给了change_data函数，把dict比作鱼缸，里面的k,v比作缸里装的鱼。现在只是把鱼缸丢给了函数，这个鱼缸本身你不能改，但是里面的鱼可以。 相当于只是传了一个对这个d的引用关系给到函数的形参。这样是为了减少内存的浪费，因为如果这个 dict 比较大，传一次到函数里就要copy一份新的值的话，效率太低了。
