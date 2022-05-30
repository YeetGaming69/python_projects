from random import randint

def check_number(num):
    while type(num) != int:
        try:
            num = int(num)
        except:
            num = input("please use a whole number: ")
    return num

sides = check_number(input("how many sides does the dice have: "))

number = randint(1, sides)
number = str(number)

print("the number is: " + number)
