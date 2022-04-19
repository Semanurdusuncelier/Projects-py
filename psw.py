import random

print("Welcome to your password generator ")


chars='qwertyuopmnbvcxzasdfghjkli7896321450+-*/?!%&<>'

number=input("Amount of passwords to generate :")

number = int(number)

length = input("Input your password length :")
length= int (length)

print("\n here are your passwords:")

for pwd in range(number):
     password =''
for a in range(length):
     password+= random.choice(chars)
     print(password)
