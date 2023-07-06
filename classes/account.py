class Account:
    bank_name ="Corparative"
    def __init__(self,account_name,account_number,account_type):
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

            #Update the withdrawal method to append each withdrawal transaction to the withdrawals list.
            #  Each transaction should be in form of a dictionary like like this {"amount": amount,"narration": “withdrawal”}
            transactions= {"amount": amount, "narration": "withdraw"}
            list=self.balance.withdrawals.append(transactions)
            return list



    def deposit(self,amount):
        self.balance +=amount
        return f"Deposit of {amount} successful. New balance is {self.balance}"
    
        #Update the deposit method to append each withdrawal transaction to the deposits list. 
        # Each transaction should be in form of a dictionary like this {"amount": amount,"narration": “deposit”}
        transaction={"amount": amount, "narration": "deposit"}
        list = self.balance.deposits.append(transaction)
        return list
    

    def check_balance(self):
        return(f"Current balance is {self.balance}")
    
    def print_statement(self):
        transactions=self.deposits+self.withdrawals
        for transaction in self.transactions:
            print({transaction["narration"]} - {transaction["amount"]})

    def borrow_loan(self,amount):
        totalDeposits=sum([transaction[amount]] for transaction in self.deposits)
        limit=totalDeposits/3


        if self.loan_balance>0:
            return f"Existing loan"
        elif amount<100:
            return f"Must be at least 100 shillings"
        elif len(self.deposits)<10:
            return f"Must have more than 10 deposits"
        elif amount>limit:
            return f"Loan requested exceeds the limit {limit}"
        else:
         self.loan_balance+=amount
         self.balance+=amount
         return f"Loan successfully approved, loan balance increased by amount{amount}"
        
    def repay_loan(self,amount):
        if amount<self.loan_balance:
            self.loan_balance-=amount 
            return f"Your new balance is {self.loan_balance}"   
        elif amount==self.loan_balance:
            return f"You have settled you loan"
    
        elif amount>self.loan_balance:
            Overbalance=amount-self.loan_balance 
            self.balance+=Overbalance
            return f"You have successfully paid your loan"

    def transfer(self,amount,recepient):
        taxCharge=10
        totalAmount=amount+(amount*taxCharge/100)
        if totalAmount< self.balance:
            recepient.deposit(amount)
            self.balance-=amount
        else:
            return f"Insufficient balance"    




        
        




