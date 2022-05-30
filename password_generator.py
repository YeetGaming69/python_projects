from random import randint

def check_number(number):
    while type(number) != int:
        try:
            number = int(number)
        except:
            number = input("Please type a whole number: ")
    return number

pass_length = check_number(input("how long should the password be?: "))
character_set = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "e", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ",", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
password = ""
character = 0
character_num = 0

while character_num < pass_length:
    character = randint(1, len(character_set))
    character -= 1
    password += character_set[character]
    character_num += 1

print(password)
