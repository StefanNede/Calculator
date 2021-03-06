# calculator
from tkinter import *

root = Tk()
root.title("calculator")
root['bg'] = '#2C4449'

operator = ""
firstNumber = 0

# entry field, for the current number to get displayed
e = Entry(root, width=34, borderwidth=4, bg="#2D3E47", fg="white", highlightbackground="#627B88")
e.grid(row=0, column=0, columnspan=4, ipady=4)

# functions for the actions
def changeOutput(number):
    newNumber = e.get() + str(number)
    e.delete(0, END)
    e.insert(0, newNumber)

# in here we will take in the first number
def operation(operatorEntered):
    global firstNumber
    global operator
    firstNumber = float(e.get())
    operator = operatorEntered
    e.delete(0, END)

# in here we will take in the second number and do whatever is stored in the
# operator variable to it, with the first number
def equals():
    global firstNumber
    global operator
    secondNumber = float(e.get())

    if operator == "+":
        result = secondNumber + firstNumber
        e.delete(0, END)
        e.insert(0, result)
    if operator == "-":
        result = firstNumber-secondNumber
        e.delete(0, END)
        e.insert(0, result)
    if operator == "÷":
        result = round(firstNumber/secondNumber, 5)
        e.delete(0, END)
        e.insert(0, result)
    if operator == "x":
        result = firstNumber*secondNumber
        e.delete(0, END)
        e.insert(0, result)
    operator = ""
    firstNumber = 0


# for plus minus, we change the first number in the input area and then add a - to the variable
def plus_minus():
    global firstNumber
    firstNumber = float(e.get()) - float(e.get())*2
    e.delete(0, END)
    e.insert(0, firstNumber)


# changes to a percentage
def percentage():
    global firstNumber
    firstNumber = float(e.get())/100
    e.delete(0, END)
    e.insert(0, firstNumber)

# deletes everything in the input box
def delete():
    global firstNumber
    global operator
    operator = ""
    firstNumber = 0
    e.delete(0, END)


# creating the buttons
# number buttons
# highlightbackground added along with bg, as only bg for buttons doesn't work on mac
button1 = Button(root, text="1", padx=30, pady=20,
                 command=lambda: changeOutput(1), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button2 = Button(root, text="2", padx=30, pady=20,
                 command=lambda: changeOutput(2), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button3 = Button(root, text="3", padx=30, pady=20,
                 command=lambda: changeOutput(3), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button4 = Button(root, text="4", padx=30, pady=20,
                 command=lambda: changeOutput(4), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button5 = Button(root, text="5", padx=30, pady=20,
                 command=lambda: changeOutput(5), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button6 = Button(root, text="6", padx=30, pady=20,
                 command=lambda: changeOutput(6), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button7 = Button(root, text="7", padx=30, pady=20,
                 command=lambda: changeOutput(7), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button8 = Button(root, text="8", padx=30, pady=20,
                 command=lambda: changeOutput(8), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button9 = Button(root, text="9", padx=30, pady=20,
                 command=lambda: changeOutput(9), highlightbackground="#657F7F", fg="white", bg="#657F7F")
button0 = Button(root, text="0", padx=70, pady=20,
                 command=lambda: changeOutput(0), highlightbackground="#657F7F", fg="white", bg="#657F7F")

# operator buttons
button_AC = Button(root, text="AC", padx=25, pady=19, command=delete, highlightbackground= "#405359", fg="white", bg="#405359")
button_plus_minus = Button(root, text="+/-", padx=25,
                           pady=18, command=plus_minus, highlightbackground= "#405359", fg="white", bg="#405359")
button_percentage = Button(root, text="%", padx=29,
                           pady=18, command=percentage, highlightbackground= "#405359", fg="white", bg="#405359")
button_divide = Button(root, text="÷", padx=29, pady=19,
                       command=lambda: operation("÷"), highlightbackground= "#FF9C26", fg="white", bg="#FF9C26")
button_multiply = Button(root, text="x", padx=30, pady=20,
                         command=lambda: operation("x"), highlightbackground= "#FF9C26", fg="white", bg="#FF9C26")
button_minus = Button(root, text="-", padx=30, pady=20,
                      command=lambda: operation("-"), highlightbackground= "#FF9C26", fg="white", bg="#FF9C26")
button_plus = Button(root, text="+", padx=29, pady=20,
                     command=lambda: operation("+"), highlightbackground= "#FF9C26", fg="white", bg="#FF9C26")
button_equal = Button(root, text="=", padx=29, pady=20, command=equals, highlightbackground= "#FF9C26", fg="white", bg="#FF9C26")
button_dot = Button(root, text="•", padx=32, pady=20,
                    command=lambda: changeOutput("."), highlightbackground="#657F7F", fg="white", bg="#657F7F")

# adding the buttons
# setting the number buttons
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button0.grid(row=5, column=0, columnspan=2)

# setting the operator buttons
button_AC.grid(row=1, column=0)
button_plus_minus.grid(row=1, column=1)
button_percentage.grid(row=1, column=2)
button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_minus.grid(row=3, column=3)
button_plus.grid(row=4, column=3)
button_equal.grid(row=5, column=3)
button_dot.grid(row=5, column=2)

root.mainloop()
