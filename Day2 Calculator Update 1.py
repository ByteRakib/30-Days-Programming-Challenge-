from tkinter import *

#create a new window
root = Tk()
root.title("Calculator")

#Create a display
display = Label(root, text="", bg="white", font=("Arial",20), anchor=E)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky=N+S+E+W)

#create the buttons
button_1=Button(root,text="1",font=("Arial",16),command=lambda: button_click("1"))
button_2=Button(root,text="2",font=("Arial",16),command=lambda: button_click("2"))
button_3=Button(root,text="3",font=("Arial",16),command=lambda: button_click("3"))
button_4=Button(root,text="4",font=("Arial",16),command=lambda: button_click("4"))
button_5=Button(root,text="5",font=("Arial",16),command=lambda: button_click("5"))
button_6=Button(root,text="6",font=("Arial",16),command=lambda: button_click("6"))
button_7=Button(root,text="7",font=("Arial",16),command=lambda: button_click("7"))
button_8=Button(root,text="8",font=("Arial",16),command=lambda: button_click("8"))
button_9=Button(root,text="9",font=("Arial",16),command=lambda: button_click("9"))
button_0=Button(root,text="0",font=("Arial",16),command=lambda: button_click("0"))
button_decimal=Button(root,text=".",font=("Arial",16),command=lambda: button_click("."))
button_add=Button(root,text="+",font=("Arial",16), command=lambda: button_operator("+"))
button_subtract=Button(root,text="-",font=("Arial",16),command=lambda:button_operator("-"))
button_multiply=Button(root,text="*", font=("Arial",16), command=lambda:button_operator("*"))
button_devide=Button(root,text="/", font=("Arial",16), command=lambda:button_operator("/"))
button_modulus=Button(root,text="%", font=("Arial",16), command=lambda:button_operator("/"))
button_square_root=Button(root, text="√", font=("Arial",16), command=lambda:button_operator("√"))
button_exponent = Button(root, text="^", font=("Arial", 16), command=lambda: button_operator("^"))
button_equals=Button(root,text="=",font=("Arial",16),command=lambda:button_equals())
button_clear=Button(root,text="C",font=("Arial",16),command=lambda:button_clear())

#position the buttons
button_1.grid(row=4,column=0, padx=10, pady=10, sticky=N+S+E+W)
button_2.grid(row=4,column=1, padx=10, pady=10, sticky=N+S+E+W)
button_3.grid(row=4,column=2, padx=10, pady=10, sticky=N+S+E+W)
button_4.grid(row=3,column=0, padx=10, pady=10, sticky=N+S+E+W)
button_5.grid(row=3,column=1, padx=10, pady=10, sticky=N+S+E+W)
button_6.grid(row=3,column=2, padx=10, pady=10, sticky=N+S+E+W)
button_7.grid(row=2,column=0, padx=10, pady=10, sticky=N+S+E+W)
button_8.grid(row=2,column=1, padx=10, pady=10, sticky=N+S+E+W)
button_9.grid(row=2,column=2, padx=10, pady=10, sticky=N+S+E+W)
button_0.grid(row=5,column=1, padx=10, pady=10, sticky=N+S+E+W)
button_decimal.grid(row=5,column=0, padx=10, pady=10, sticky=N+S+E+W)
button_add.grid(row=5,column=3, padx=10, pady=10, sticky=N+S+E+W)
button_subtract.grid(row=4,column=3, padx=10, pady=10, sticky=N+S+E+W)
button_multiply.grid(row=3,column=3, padx=10, pady=10, sticky=N+S+E+W)
button_devide.grid(row=2, column=3, padx=10, pady=10, sticky=N+S+E+W)
button_modulus.grid(row=1, column=3, padx=10, pady=10, sticky=N+S+E+W)
button_square_root.grid(row=1, column=1, padx=10, pady=10, sticky=N+S+E+W)
button_exponent.grid(row=1, column=2, padx=10, pady=10, sticky=N+S+E+W)
button_equals.grid(row=5, column=2, padx=10, pady=10, sticky=N+S+E+W)
button_clear.grid(row=1, column=3, padx=10, pady=10, sticky=N+S+E+W)

#Create function to operate the calculator
def button_click(number):
	current=display.cget("text")
	display.configure(text=current+number)
	
def button_operator(operator):
	global first_num, operation
	operation=operator
	first_num=float(display.cget("text"))
	display.configure(text="")
	
def button_equals():
    second_num = float(display.cget("text"))
    display.configure(text="")
    if operation == "+":
        result = first_num + second_num
    elif operation == "-":
        result = first_num - second_num
    elif operation == "*":
        result = first_num * second_num
    elif operation == "/":
        result = first_num / second_num
    elif operation == "%":
        result = first_num % second_num
    elif operation == "sqrt":
        result = first_num ** 0.5
    elif operation == "^":
        result = first_num ** second_num
    display.configure(text=result)

def button_clear():
	display.configure(text="")
	
root.mainloop()
