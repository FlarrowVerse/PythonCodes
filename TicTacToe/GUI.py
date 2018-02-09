from graphics import *

win = GraphWin("Tic-Tac-Toe", 300, 300)
win.setBackground("yellow")

l1 = Line(Point(100,0), Point(100,300))
l1.setFill("blue")
l1.setWidth(10)
l1.draw(win)

l2 = Line(Point(200,0), Point(200,300))
l2.setFill("blue")
l2.setWidth(10)
l2.draw(win)

l3 = Line(Point(0,100), Point(300,100))
l3.setFill("blue")
l3.setWidth(10)
l3.draw(win)

l4 = Line(Point(0,200), Point(300,200))
l4.setFill("blue")
l4.setWidth(10)
l4.draw(win)

seeds = ['X', 'O']
colors = ['red', 'black']
for i in range(9):
    pt = win.getMouse()
    seed = Text(pt, seeds[i%2])
    seed.setFill(colors[i%2])
    seed.setSize(36)
    seed.draw(win)


win.close()