from tkinter import *


global number1, number2
global second, sign
second = 0
number1, number2 = "0", "0"


class Number:
    def __init__(self, num, row_, column_):
        Button(window, text=num, bd=0, font=('Arial', 15, "bold"),
               bg="black", fg=rgb((230, 230, 230)),
               command=lambda:  count(num)
               ).grid(row=row_, column=column_, padx=1, pady=1, sticky='WSEN')


class Function:
    def __init__(self, text, fun, row_, column_):
        Button(window, text=text, bd=0, font=('Arial', 15),
               bg=rgb((20, 20, 20)), fg=rgb((230, 230, 230)),
               command=lambda: action(fun)
               ).grid(row=row_, column=column_, padx=1, pady=1, sticky='WSEN')


def count(x):
    global number1, number2
    if second == 0:
        if number1 == '0':
            number1 = str(x)
        else:
            number1 += str(x)
        label.configure(text=number1)
    else:
        if number2 == '0':
            number2 = str(x)
        else:
            number2 += str(x)
        label.configure(text=number2)


def calculate(x):
    global number1, number2, second, sign
    if sign == 'plus':
        a = float(number1)+float(number2)
    elif sign == 'minus':
        a = float(number1)-float(number2)
    elif sign == 'multiple':
        a = float(number1)*float(number2)
    else:
        a = float(number1)/float(number2)

    if x == 1:
        return a
    else:
        number1, number2 = "0", "0"
        second = 0
        label.configure(text=round(a, 4))


def action(x):
    global number1, number2, second, sign
    if x == "clear":
        number1, number2 = "0", "0"
        label.configure(text=number1)
    elif x == "delete":
        if second == 0:
            number1 = number1[:-1]
            label.configure(text=number1)
        else:
            number2 = number2[:-1]
            label.configure(text=number2)
    elif second == 0:
        second = 1
        sign = x
        label.configure(text=number2)
    else:
        number1 = calculate(1)
        number2 = '0'
        sign = x
        label.configure(text=number2)


def rgb(value):
    return "#%02x%02x%02x" % value


window = Tk()
window.configure(bg=rgb((35, 35, 35)))
window.grid_columnconfigure((0, 1, 2, 3), weight=1)
window.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
window.title("calculator")

window.geometry('250x300+200+200')

label = Label(window, text="0", font=('Arial', 30, "bold"),
              bg=rgb((35, 35, 35)), fg=rgb((230, 230, 230)))

devide_button = Function('/', "devide", 1, 0)
multiple_button = Function('x', "multiple", 1, 1)
clear_button = Function('C', "clear", 1, 2)
delete_button = Function('<', "delete", 1, 3)
plus_button = Function('+', "plus", 2, 3)
minus_button = Function('-', "minus", 3, 3)
calculate_button = Button(window, text="=", bd=0, font=('Arial', 15),
                          bg=rgb((25, 50, 100)), fg=rgb((230, 230, 230)),
                          command=lambda: calculate(0))

one_button = Number('1', 4, 0)
two_button = Number('2', 4, 1)
three_button = Number('3', 4, 2)
four_button = Number('4', 3, 0)
five_button = Number('5', 3, 1)
six_button = Number('6', 3, 2)
seven_button = Number('7', 2, 0)
eight_button = Number('8', 2, 1)
nine_button = Number('9', 2, 2)
zero_button = Number('0', 5, 1)
dot_button = Number('.', 5, 2)


label.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky='WSEN')

calculate_button.grid(row=4, rowspan=2, column=3,
                      padx=1, pady=1, sticky='WSEN')


window.mainloop()
