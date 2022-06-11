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


