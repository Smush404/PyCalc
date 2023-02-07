import os 
import time

def clear():
    command = "clear"
    os.system(command)
def fslashs(intake):
    symbol = intake
    print(symbol*60)
def prints(text):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(.05)
    print()

wait = 1.5
user = 0
clear()

while(user != 5):
    prints("/"*60)
    prints(" "*24 + "Hello There!")
    prints("\\"*60)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Muliplcation")
    print("4. Division")
    print("5. Expentent")
    print("6. Exit")
    print("\nInput:", end=' #')
    user = int(input())
    print()
    clear()

    if user == 6:
        prints("\\"*60)
        prints(" "*24 + "Bye Bye!".title())
        prints("/"*60)
        time.sleep(wait)
        break

    elif(user == 1):
        prints("+"*60)
        prints(" "*24 + "Addition")
        prints("+"*60)
        print("\nenter number 1", end=' #')
        num1 = int(input())
        print("enter number 2", end=' #')
        num2 = int(input())
        fslashs("=")
        print(num1,"+",num2,"equals",(num1 + num2))
        print("{}".format("wait"))
        time.sleep(wait)


    elif(user == 2):
        fslashs("-")
        print("{:^60}".format("Subtraction"))
        fslashs("-")
        print("\nenter number 1", end=' #')
        num1 = int(input())
        print("enter number 2", end=' #')
        num2 = int(input())
        fslashs("=")
        print(num1,"-",num2,"equals",(num1 - num2))
        print("{}".format("wait"))
        time.sleep(wait)

    elif(user == 3):
        fslashs("*")
        print("{:^60}".format("Muliplcation"))
        fslashs("*")
        print("\nenter number 1", end=' #')
        num1 = int(input())
        print("enter number 2", end=' #')
        num2 = int(input())
        fslashs("=")
        print(num1,"*",num2,"equals",(num1 * num2))
        print("{}".format("wait"))
        time.sleep(wait)

    elif(user == 4):
        fslashs("/")
        print("{:^60}".format("Division"))
        fslashs("/")
        print("\nenter number 1", end=' #')
        num1 = int(input())
        print("enter number 2", end=' #')
        num2 = int(input())
        fslashs("=")
        print(num1,"/",num2,"equals","{:.2f}".format(num1 / num2))
        print("{}".format("wait"))
        time.sleep(wait)
    elif(user == 5):
        fslashs("/")
        print("{:^60}".format("expentent"))
        fslashs("/")
        print("\nenter number 1", end=' #')
        num1 = int(input())
        print("enter number 2", end=' #')
        num2 = int(input())
        fslashs("=")
        print(num1,"^",num2,"equals","{:.2f}".format(num1 ** num2))
        print("{}".format("wait"))
        time.sleep(wait)
    clear()

clear()