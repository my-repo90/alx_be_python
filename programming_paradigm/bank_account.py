class BankAccount:
    def __init__(self , account_balance = 0):
        self.account_balance = account_balance

    # Implement deposit(amount), withdraw(amount), and display_balance() methods.
    def deposit(self , amount):
        if amount > 0:    
            self.account_balance =+ amount
            return amount
        else :
            ammount = None

    def withdraw(self , amount):
        if amount > self.account_balance :
            amount = None
        else :
            self.account_balance =- amount
            return True 
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance :.2f}")
