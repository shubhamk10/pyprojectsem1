from tkinter import *
import pygame as p

root = Tk()

def temptext(u):
    e.delete(0,"end")

root.title("Input for N QUEENS")
e = Entry(root, width=50, borderwidth=5,font="Calibri 10")
e.insert(0,"Enter the size of chessboard...")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.bind("<FocusIn>",temptext)




def buttonadd(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


def buttoninsert():
    global f
    f = int(e.get())
    e.delete(0, END)
    root.destroy()


def buttonclear():
    e.delete(0, END)


button_1 = Button(root, text="1", padx=50, pady=30, command=lambda: buttonadd(1))
button_2 = Button(root, text="2", padx=50, pady=30, command=lambda: buttonadd(2))
button_3 = Button(root, text="3", padx=50, pady=30, command=lambda: buttonadd(3))
button_4 = Button(root, text="4", padx=50, pady=30, command=lambda: buttonadd(4))
button_5 = Button(root, text="5", padx=50, pady=30, command=lambda: buttonadd(5))
button_6 = Button(root, text="6", padx=50, pady=30, command=lambda: buttonadd(6))
button_7 = Button(root, text="7", padx=50, pady=30, command=lambda: buttonadd(7))
button_8 = Button(root, text="8", padx=50, pady=30, command=lambda: buttonadd(8))
button_9 = Button(root, text="9", padx=50, pady=30, command=lambda: buttonadd(9))
button_0 = Button(root, text="0", padx=50, pady=30, command=lambda: buttonadd(0))
button_insert = Button(root, text="Insert", padx=90, pady=40, command=buttoninsert)
button_clear = Button(root, text="CLEAR", padx=40, pady=20, command=buttonclear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_insert.grid(row=4, column=1, rowspan=2, columnspan=2)
button_clear.grid(row=5, column=0)

root.mainloop()

if f < 4:
    print("Value less than 4 is not valid\nTaking the value of n as 4...")
    f = 4

h, w = 800, 800
sqs = h // f

board = []
board1 = []
board2 = []


def getBoard():
    for i in range(f):
        nthList = []
        for j in range(f):
            nthList.append(0)
        board.append(nthList)


def printBoard():
    for i in range(f):
        board1.append(((i + 1) * (800 // f)) - (800 // (2 * f)))
        for j in range(f):
            if board[i][j] == 1:
                board[i][j] = ((j + 1) * (800 // f)) - (800 // (2 * f))
            print(board[i][j], end=" ")
        print("")


def isSafe(row, col):
    for i in range(f):
        if board[row][i] == 1:
            return False
    for j in range(f):
        if board[j][col] == 1:
            return False

    i = row - 1
    j = col - 1
    while (i >= 0 and j >= 0):
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    i = row - 1
    j = col + 1
    while (i >= 0 and j < f):
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    i = row + 1
    j = col - 1
    while (i < f and j >= 0):
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1

    i = row + 1
    j = col + 1
    while (i < f and j < f):
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j + 1
    return True


def Put(f, count):
    if count == f:
        return True
    for i in range(f):
        for j in range(f):
            if isSafe(i, j):
                board[i][j] = 1
                count = count + 1
                if Put(f, count) == True:
                    return True
                board[i][j] = 0
                count = count - 1
    return False


getBoard()
Put(f, 0)

printBoard()

for l in range(f):
    for m in range(f):
        if board[l][m] > 0:
            board2.append(board[l][m])

p.init()
scr = p.display.set_mode((h, w))
p.display.set_caption("N QUEENS")
a=p.image.load('crown.png')
p.display.set_icon(a)
scr.fill(p.Color("white"))
colour = [p.Color("white"), p.Color("gray")]
pchess = []
b1 = []
b2 = []
for c in range(f):
    pchess.append(p.image.load('queen-chess-piece-black-shape.png'))


def loadimg(X, Y, c):
    scr.blit(pchess[c], (X, Y))


for i in range(f):
    for j in range(f):
        collor = colour[((i + j) % 2)]
        p.draw.rect(scr, collor, p.Rect(j * sqs, i * sqs, sqs, sqs))
run = True
p.display.flip()
while run:
    for x in p.event.get():
        if x.type == p.QUIT:
            run = False
    for k in range(f):
        loadimg(board1[k], board2[k], k)
    p.display.update()
