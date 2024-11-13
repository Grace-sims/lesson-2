import turtle as t

y = input("what is the color of a star?")
d = input("what is the color of the background?")
w = input("wth is the width?")

t.bgcolor (d)

t.color (y)

t.width (w)

for x in range (5):
    t.forward(100)
    t.right(144)

t.mainloop ()