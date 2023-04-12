# display welcome message
print("Welcome to the Simple Calculator program!\n")

# ask user for first number
while True:
    try:
        num1 = float(input("Please enter the first number: "))
        break
    except ValueError:
        print("Oops! That wasn't a valid number. Please try again.\n")

# ask user for operation to perform
while True:
    op = input("Please enter the operation to perform (+, -, *, /): ")
    if op in ['+', '-', '*', '/']:
        break
    else:
        print("Oops! That wasn't a valid operation. Please try again.\n")

# ask user for second number
while True:
    try:
        num2 = float(input("Please enter the second number: "))
        break
    except ValueError:
        print("Oops! That wasn't a valid number. Please try again.\n")

# perform calculation based on user input
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
else:
    result = num1 / num2

# display result to user
print(f"\n{num1} {op} {num2} = {result}")
