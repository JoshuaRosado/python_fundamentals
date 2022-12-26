
class User:
    def __init__(self, name = "Unassigned", int_rate = 0.02, balance = 0):
        self.name = name
        self.account = Bank_Account(int_rate, balance)
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def with_draw(self, amount):
        self.account.with_draw(amount)
        return self
    
    def display_user_balance(self):
        print(f"Balance:{self.name}")
        self.account.display_account_info()
        return self
    
    def yield_interest(self):
        self.account.yield_interest()
        return self
    












class Bank_Account:
    
    all_accounts = []
    def __init__(self, int_rate=0.2, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_accounts.append(self)
    
    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.balance += amount
        return self
    
    def with_draw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            print("Withdrawing$" + str(amount))
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("=====================")
        print(f"Account Balance: ${self.balance}")
        print(f"Interest Rate: {self.int_rate}")
        print("=====================")
        return self
    
    
    
    
    def yield_interest(self):
        print("Yielding Interest...")
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()
    
    @classmethod
    def all_balance(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
            
        
        

joshua_account = User("Joshua's Account")
alexis_account = User("Account of Alexis")

joshua_account.display_user_balance().make_deposit(100).display_user_balance()
joshua_account.with_draw(50).display_user_balance().make_deposit(950).make_deposit(400).make_deposit(1575).yield_interest().display_user_balance()

alexis_account.display_user_balance().make_deposit(2050).make_deposit(1000).display_user_balance().yield_interest().display_user_balance()

