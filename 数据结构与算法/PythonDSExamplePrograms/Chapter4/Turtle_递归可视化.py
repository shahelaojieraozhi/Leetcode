import turtle

t = turtle.Turtle()

'''画正方形
# 指挥向前100
# t.forward(100)
for i in range(4):
    t.forward(100)  # 前进多少米
    t.right(270)    # 向右转多少度
'''

# 画五角星
t.pencolor("red")
t.pensize(3)
for i in range(5):
    t.forward(100)
    t.right(144)
t.hideturtle()  # 隐藏箭头

# 作图完毕
turtle.done()
