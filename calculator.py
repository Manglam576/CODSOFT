import os
import platform
def clear_screen():
    if platform.system()== "Windows":
        os.system("cls")
    else:
        os.system("clear")
clear_screen()
while True:
    a = int(input("enter your number:"))
    b = int(input("enter your number:"))
    print(" enter a operation(*,/,+,-)")
    o = input("enter your operation:")
    if o == "+":
        print(a+b)
    elif o == "-":
        print(a-b)
    elif o == "/":
        print(a/b)
    elif o == "*":
        print(a*b)
    else:
        print("invalid input")
    print("----------------")


