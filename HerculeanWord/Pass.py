import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to HerculeanWord!!")
lenLetters = int(input("Enter the Number of Letters you want in your Password:\n"))
lenNumbers = int(input(f"Enter the Number of Numbers you want in your Password:\n"))
lenSymbols = int(input("Enter the Number of Symbols you want in your Password:\n"))

PasswordList = []
for letter in range(1, lenLetters + 1):
    PasswordList.append(random.choice(letters))
for number in range(1, lenNumbers + 1):
    PasswordList.append(random.choice(numbers))
for symbol in range(1, lenSymbols + 1):
    PasswordList.append(random.choice(symbols))

random.shuffle(PasswordList)
Password = ''
for key in PasswordList:
    Password += key

print(f"Your Powerful Password is {Password}")
