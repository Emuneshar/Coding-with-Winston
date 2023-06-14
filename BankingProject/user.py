class user:

    # This is our constructor function
    
    def __init__ (self, firstName, lastName, userName, password, accountNumber, accountBalance):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance

    # Getter and setter functions
    # Each one must take "self" as a parameter 

    # Getter
    def getFirstName(self):
        return self.firstName
    
    # Setter
    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    