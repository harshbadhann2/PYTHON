
# PASSWORD MANAGER

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':',';','<',',','>','.','/','?']

print('WELCOME TO PASSWORD MANAGER! //Generared by BADHANN')

pass_letter = int(input("Enter the number of letters need to be in password: "))
pass_number = int(input("Enter the number of numbers need to be in password: "))
pass_symbol = int(input("Enter the number of symbols need to be in password: "))

password = ''
for char in range(0,pass_letter):
    password += random.choice(letters)

for num in range(0,pass_number):
    password += random.choice(numbers)

for sym in range(0,pass_symbol):
    password += random.choice(symbols)

print(password)