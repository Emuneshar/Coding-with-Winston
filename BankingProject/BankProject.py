import random
import os

print("Welcome to the Bank of Coach Eshwar")
print("If you don't have an account you can open one now by selecting 1 from the menu below")
print(
    "Your options are as follows:\n"
    
    "1. Open an account\n",
    "2. Deposit Money\n",
    "3. Withdraw Money\n",
    "4. View Balance\n",
    "5. Open a credit card\n"
)

def openAccount():
    User = dict(username = "", password = "", accountNumber = 0)
    username = input(str("What would you like to be your username\n"))
    password = input(str("Please create your password\n"))
    accountNumber = random.randint(99999999, 999999999999)
    userName = (username)
    passWord = (password)
    User[username] = userName
    User[password] = passWord
    User[accountNumber] = accountNumber
    return User
    

listOfAccounts = []

selected = int(input("Which one would you like?"))



match selected:
    case 1:
        listOfAccounts.append(openAccount())
        print(listOfAccounts[0])
    case 2:
        username = str(input("what is your username?"))
        if username in listOfAccounts:
            print("Account found!")
            deposit = float(input("How much would you like to deposit?"))
        else:
            print("Account not found")






