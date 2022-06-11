# from pythonds.basic.queue import Queue

class Queue:
    def __init__(self):
        self.items = []     # 空队列用空列表表示

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hotPotato(namelist, num):
    # 新建队列
    simqueue = Queue()
    # 添加数据
    for name in namelist:
        simqueue.enqueue(name)

    # FIFO
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 9))
#  nums = 9 ，表示传递9次
