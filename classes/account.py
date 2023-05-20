class Account:
    bank_name ="Corparative"
    def __init__(self,account_name,account_number,balance,account_type):
        self.account_name= account_name
        self.account_number= account_number
        self.balance= balance
        self.account_type= account_type

    def withdraw(self,amount):
        if amount> self.balance:
            return f"Insufficient balance."
        else:
            self.balance -=amount
            return f"Withdrawal of{amount} successful.New balance is {self.balance}."

    def deposit(self,amount):
        self.balance +=amount
        return f"Deposit of {amount} successful. New balance is {self.balance}"

    def check_balance(self):
        return f"Current balance is {self.balance}"
