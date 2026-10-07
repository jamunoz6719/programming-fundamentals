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
if opt == 1 :
    add = num1 + num2
    print(f"The additions is: {add}")
if opt == 2 :
    sub = num1 - num2
    print(f"The substraction is: {sub}")
if opt == 3 :
    mult = num1 * num2
    print(f"The multiplication is: {mult}")
if opt == 4 :
    div = num1 / num2
    print(f"The dividition is: {div}")
if opt == 5 :
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    print(f"The all operations is: \n additions {add} \n substraction {sub} \n multiplication {mult} \n dividition {div}  ")

if opt < 1 or opt > 5:
    print("Invalidation the option, please try again")
