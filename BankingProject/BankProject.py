import random
import os

print("Welcome to the Bank of Coach Eshwar")
print("If you don't have an account you can open one now by selecting 1 from the menu below")
print(
    "Your options are as follows:\n"
    
    "1. Open an account\n",
    "2. Destroy your computer\n",
    "3. Steal from bank\n",
    "4. Get captured by the FBI\n",
    "5. Open a credit card\n"
)

def openAccount():
    User = dict(username = "", password = "", accountNumber = 0)
    username = input(str("What would you like to be your username"))
    password = input(str("Please create your password"))
    accountNumber = random.randint(99999999, 999999999999)
    userName = (username)
    passWord = (password)
    User[username] = userName
    User[password] = passWord
    User[accountNumber] = accountNumber
    print(User[username])
    

selected = int(input("Which one would you like?"))

match selected:
    case 1:
        openAccount()


