import random
import pyperclip
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_{|}~"
password = ''
try:
    passwordLength = int(input("How long do you want your password to be?"))
except ValueError:
    passwordLength = int(input("Please enter a digit!"))
for i in range(passwordLength):
    password = password + random.choice(characters)
print(password)
