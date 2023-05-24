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
    # get user information

selected = int(input("Which one would you like?"))

match selected:
    case 1:
        openAccount()


