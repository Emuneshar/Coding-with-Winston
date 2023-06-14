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
    User = dict(username = "", password = "", accountNumber = 0, balance = 0 )
    userN = input(str("What would you like to be your username\n"))
    passW = input(str("Please create your password\n"))
    startingBalance = float(input("how much would you like to deposit?"))
    accountNumber = random.randint(99999999, 999999999999)
    # userName = (username)
    # passWord = (password)
    User["username"] = userN
    User["password"] = passW
    User["accountNumber"] = accountNumber
    User["balance"] = startingBalance
    return User
    

listOfAccounts = []


while True:

    selected = int(input("Which one would you like?"))



    match selected:
        case 1:
            listOfAccounts.append(openAccount())
            print(listOfAccounts)
            continue
        case 2:
            username = str(input("what is your username?"))
            if username in listOfAccounts:
                print("Account found!")
                deposit = float(input("How much would you like to deposit?"))
            else:
                print("Account not found")
        case 3:
            name = input("What is your username?")
            




