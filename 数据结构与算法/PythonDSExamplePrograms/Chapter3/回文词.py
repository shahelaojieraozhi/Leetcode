from pythonds.basic.deque import Deque

# def palchecker(aString):
#     chardeque = Deque()
#
#     for ch in aString:
#         chardeque.addRear(ch)
#
#     stillEqual = True
#
#     while chardeque.size() > 1 and stillEqual:
#         first = chardeque.removeFront()
#         last = chardeque.removeRear()
#         if first != last:
#             stillEqual = False
#
#     return stillEqual
#
# print(palchecker("lsdkjfskf"))
# print(palchecker("radar"))


def palchecker(aString):
    chardeque = Deque()

    for char in aString:
        chardeque.addRear(char)

    beep = True
    while chardeque.size() > 1 and beep:
        rear = chardeque.removeRear()
        front = chardeque.removeFront()
        if rear == front:
            beep = True
        else:
            beep = False
    return beep

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))



