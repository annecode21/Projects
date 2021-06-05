import random

print ("Welcome to my random password generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%&"
number = int(input("Number of password(s) to generate: "))
length = int(input("Enter length of password required: "))
print ("\nHere is/are your password(s): ")

for pwd in range (number):
    password = " "
    for char in range (length):
        password += random.choice(chars)
    print (password)