# password manager that creates the password with choice of own characters

import random

print('WELCOME TO PASSWORD MANAGER! //Generared by BADHANN')

pass_char = input("Enter the characters which you want to use in password (including aphabets, numbers, symbols): ")

pass_list = []
for char in range(0,len(pass_char)):
    pass_list += random.choice(pass_char)

random.shuffle(pass_list)

password = ''
for char in pass_list:
    password += char

print("The generated password is: " + password)

