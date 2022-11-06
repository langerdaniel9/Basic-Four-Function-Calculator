from tkinter import Tk, Entry, END, Button

root = Tk()
root.title("Calculator")

e = Entry(root, width=28, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, pady=10)


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def add():
    num1 = e.get()
    e.delete(0, END)
    e.insert(0, num1 + " + ")


def subtract():
    num1 = e.get()
    e.delete(0, END)
    e.insert(0, num1 + " - ")


def multiply():
    num1 = e.get()
    e.delete(0, END)
    e.insert(0, num1 + " * ")


def divide():
    num1 = e.get()
    e.delete(0, END)
    e.insert(0, num1 + " / ")


def enter():
    equation = e.get()
    answer = round(eval(equation), 8)
    e.delete(0, END)
    e.insert(0, answer)


fontSize = 18
xPadding1 = 15
xPadding2 = 7
yPadding1 = 5
yPadding2 = 8
borderWidth = 7

Button1 = Button(root, text="1", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("1"))
Button2 = Button(root, text="2", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("2"))
Button3 = Button(root, text="3", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("3"))
Button4 = Button(root, text="4", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("4"))
Button5 = Button(root, text="5", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("5"))
Button6 = Button(root, text="6", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("6"))
Button7 = Button(root, text="7", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("7"))
Button8 = Button(root, text="8", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("8"))
Button9 = Button(root, text="9", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("9"))
Button0 = Button(root, text="0", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("0"))
Buttondot = Button(root, text=".", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=lambda: click("."))
Buttonclear = Button(root, text="Clear", padx=xPadding2, pady=yPadding2, borderwidth=borderWidth, command=clear)
Buttonenter = Button(root, text="Enter", padx=xPadding2, pady=yPadding2, borderwidth=borderWidth, command=enter)
Buttonadd = Button(root, text="+", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=add)
Buttonsubtract = Button(root, text="-", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=subtract)
Buttonmultiply = Button(root, text="*", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=multiply)
Buttondivide = Button(root, text="/", padx=xPadding1, pady=yPadding1, borderwidth=borderWidth, font=fontSize, command=divide)

Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)
Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)
Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)
Button0.grid(row=4, column=1)
Buttondot.grid(row=4, column=0)
Buttonclear.grid(row=0, column=4)
Buttonenter.grid(row=4, column=2)
Buttonadd.grid(row=4, column=4)
Buttonsubtract.grid(row=3, column=4)
Buttonmultiply.grid(row=2, column=4)
Buttondivide.grid(row=1, column=4)

root.mainloop()