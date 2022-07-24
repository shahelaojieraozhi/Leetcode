class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        ''' 节点本身的自带两个属性：
                数据项本身data
                指向下一个节点的引用信息'''

    # 获取data
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# temp = Node(93)
# print(temp.getNext())
# print(temp.getData())
# print(temp.setData(64))

class zhi_list():
    def __init__(self):
        self.head = None  # 头部储存的是下一个节点的指针

    # 判断一个无序表是不是为空，只要看头部(列表头节点)是不是空的
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        # 实例化一个临时的节点
        temp = Node(item)  # temp.data = item ，这时temp.next = None
        temp.setNext(self.head)  # temp.data = item ，这时temp.next = self.head
        self.head = temp  # 头部储存的是下一个节点的指针

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current:
            if current.getData() == item:  # 这里不能current.getData== item：
                return True
            current = current.getNext()
        return False

    # def remove(self, item):
    #     self.add(-1000)
    #     pre = self.head
    #     while pre.getNext():
    #         if pre.getNext().getData() == item:  # 如果两数相等时
    #             pre.setNext(pre.getNext().getNext())
    #         else:
    #             pre = pre.getNext()
    #     return pre.getNext()

    def remove(self, item):
        # 只能删除一个数
        current = self.head
        previous = None
        found = True
        while found:
            if current.getData() == item:
                found = False
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


rz_list = zhi_list()
rz_list.add(13)
rz_list.add(11)
rz_list.add(4)
rz_list.add(4)
rz_list.add(8)
print(rz_list.length())
# print(rz_list.search((100)))

rz_list.remove((4))
print(rz_list.length())
