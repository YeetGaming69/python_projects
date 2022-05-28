def check_number(num):
    while type(num) != float:
        try:
            num = float(num)
        except:
            num = input("please use a number: ")
    return num

def check_operation(operation):
    correct_operation = False
    while correct_operation != True:
        if operation == "+":
            correct_operation = True
        elif operation == "-":
            correct_operation = True
        elif operation == "/":
            correct_operation = True
        elif operation == "*":
            correct_operation = True
        else:
            operation = input("please use +, -, / or *: ")
    return operation

def calculate(num_1, num_2, operation,):
    num_3 = 0
    if operation == "+":
        num_3 = num_1 + num_2
    elif operation == "-":
        num_3 = num_1 - num_2
    elif operation == "/":
        num_3 = num_1 / num_2
    elif operation == "*":
        num_3 = num_1 * num_2
    return num_3

num_1 = check_number(input("first number: "))
operation = check_operation(input("operation: "))
num_2 = check_number(input("second number: "))

num_3 = calculate(num_1, num_2, operation)

print(str(num_3))