login = input("Please enter your username: ")
password = input("Please enter your password: ")
if login == "user" and password == "1234":
    num1 = int(input("Please enter the first number: "))
    oper = input("Please enter the operation: ")
    num2 = int(input("Please enter the second number: "))
    if oper == "+":
        print(num1 + num2)
    if oper == "-":
        print(num1 - num2)
    if oper == "*":
        print(num1 * num2)
    if oper == "/":
        print(num1 / num2)
else:
    print("Wrong username or password")