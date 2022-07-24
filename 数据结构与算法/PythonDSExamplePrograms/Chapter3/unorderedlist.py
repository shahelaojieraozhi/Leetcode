# Node类 节点(node）是构建链表的基本数据结构。
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None    # 下个节点接地

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

# temp = Node(93)
# temp.getData()
# print(temp.getData())


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp    # 头部储存下一个节点的指针

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

# print(mylist.length())  # 6
# print(mylist.search(93))    # True
# print(mylist.search(100))   # False

mylist.add(100)
# print(mylist.search(100))   # True
# print(mylist.length())  # 7

mylist.remove(54)
print(mylist.length())  # 6
mylist.remove(93)
print(mylist.length())  # 5
mylist.remove(31)
print(mylist.length())  # 4
print(mylist.search(93))    # False
