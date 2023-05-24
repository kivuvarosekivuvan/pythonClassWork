class Account:
    bank_name ="Corparative"
    def __init__(self,account_name,account_number,balance,account_type,deposits,withdrawals,loan_balance,transactions):
        self.account_name= account_name
        self.account_number= account_number
        self.balance= 0
        self.account_type= account_type
        self.deposits=[]
        self.withdrawals=[]
        self.loan_balance=0
        self.transactions=[]


    def withdraw(self,amount):
        if amount> self.balance:
            print(f"Insufficient balance.")
        else:
            self.balance -=amount
            print(f"Withdrawal of{amount} successful.New balance is {self.balance}.") 

            #Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction should be in form of a dictionary like like this {"amount": amount,"narration": “withdrawal”}
            self.withdrawals.append({"amount": amount, "narration": "withdraw"})
            balance=sum(transaction["amount"] for transaction in withdrawals)



    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}")

        #Update the deposit method to append each withdrawal transaction to the deposits list. Each transaction should be in form of a dictionary like this {"amount": amount,"narration": “deposit”}
        self.deposits.append({"amount": amount, "narration": "deposit"})
        balance = sum(transaction["amount"] for transaction in deposits)        #list comprehension
        return balance
    

    def check_balance(self):
        print(f"Current balance is {self.balance}")

#Add a new method  print_statement which combines both deposits and withdrawals into one list and, using a for loop, prints each transaction in a new line like this
#deposit - 1000
#withdrawal - 500
    def print_statement(self):
        for transaction in self.transactions:
            transaction_type, amount=transaction
            print(f"{transaction_type}  -  {amount}")


# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
    def borrow_loan(self,amount):
        if self.loan_balance>0:
            return "Outstanding loan already"
        if amount<100:
            return "Loan limit low, it must be more than 100"
        if len(self.deposits)<10:
            return "Less deposits, must have at least 10 deposits"
        
        if amount>(1/3*sum(self.deposits)):
            return "Loan not applicable"
        
        self.loan_balance+=amount
        return "Loan successfully borrowed"
    
# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
    def repay_loan(self,amount):
        if amount<=self.loan_balance:
            self.loan_balance-=amount
            
        else:
            Overbalance=amount-self.loan_balance
            self.balance=0
            self.balance+=Overbalance


# Add a transfer method which accepts two attributes (amount and instance of another account).
# If the amount is less than the current instances balance, the method transfers the requested 
# amount from the current account to the passed account. The transfer is accomplished by reducing 
# the current account balance and depositing the requested amount to the passed account.        
    def transfer(self,amount,recepient):
        if amount<=self.balance:
            self.balance-=amount
            recepient.deposit(amount)
            self.transactions.append(("transfer", - amount))
            recepient.transactions.append(("transfer", - amount))

        else:
            return "Insufficient balance"    
        





































