# Import packages
import os
from random import randint

#Inizialize
num1= randint(-100, 100)
num2= randint(-100, 100)
div=0
sub=0
add=0
mult=0
opt=0
os.system("clear")
print("Welcome to the calculator v2.0")
#Get data (Imputs)
print(f"Your numeber one is: {num1}, Your number two is: {num2} ")
print(num1, num2)
print("Your number one is ", num1, "Your number two is", num2)
#Display the options
print("MAIN MENU")
print("[1]. addtion \n[2]. Substraction \n[3]. multiplication \n[4]. Dividition \n[5]. All Operations")
opt = int(input("Please enter your option[1, 5]: "))
match opt:
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        print(num1 /num2)
    case 5:
        print(num1 + num2, num1 - num2, num1 * num2, num1 / num2)
    case _:
        print("error")
        



