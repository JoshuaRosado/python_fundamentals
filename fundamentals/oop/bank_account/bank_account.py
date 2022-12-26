class Bank_Account:
    
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def with_draw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("=====================")
        print(f"Balance:{self.balance}")
        print("=====================")
        return self
    
    
    
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        
        

account_1 = Bank_Account(200.5, 10000)
account_2 = Bank_Account(200.5, 2000)







# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)


account_1.deposit(25).deposit(25).deposit(50).with_draw(50).yield_interest().display_account_info()


# 
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)


account_2.deposit(50).deposit(50).with_draw(150).with_draw(100).with_draw(150).with_draw(100).yield_interest().display_account_info()


Bank_Account.print_all_accounts()