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
            return f"Insufficient balance"
        else:
            self.balance -=amount
            return f"Withdrawal of{amount} successful.New balance is {self.balance}."

            #Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction should be in form of a dictionary like like this {"amount": amount,"narration": “withdrawal”}
            self.withdrawals.append({"amount": amount, "narration": "withdraw"})
            balance=sum(transaction["amount"] for transaction in withdrawals)



    def deposit(self,amount):
        self.balance +=amount
        return f"Deposit of {amount} successful. New balance is {self.balance}"
        self.deposits.append({"amount": amount, "narration": "deposit"})
        balance = sum(transaction["amount"] for transaction in deposits)        #list comprehension
        return balance
    
        #Update the deposit method to append each withdrawal transaction to the deposits list. Each transaction should be in form of a dictionary like this {"amount": amount,"narration": “deposit”}
        self.deposits.append({"amount": amount, "narration": "deposit"})
        balance = sum(transaction["amount"] for transaction in deposits)        #list comprehension
        return balance
    

    def check_balance(self):
        return(f"Current balance is {self.balance}")
    
    def print_statement(self):
        for transaction in self.transactions:
            transaction_type,amount=transaction
            print({transaction_type} - {amount})

    def borrow_loan(self,amount):
        if self.loan_balance>0:
            return "Existing loan"
        if amount<100:
            return "Must be at least 100 shillings"
        if len(self.deposits)<10:
            return "Must have more than 10 deposits"
        if amount>1/3*sum(self.deposits):
            return "Loan not applicable"
        else:
         self.loan_balance+=amount
         return "Loan successfully approved, loan balance increased by amount09"
        
    def repay_loan(self,amount):
        if amount<self.loan_balance:
            self.loan_balance-=amount    
        else:
            Overbalance=amount-self.loan_balance 
            Overbalance+=self.balance

    def transfer(self,amount,recepient):
        if amount< self.balance:
            recepient+=amount
            self.balance-=amount




        
        




