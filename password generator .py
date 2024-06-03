import random
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

selection_list = letters + digits + special_chars

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(special_chars))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(digits))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your random password to use is: {password}")