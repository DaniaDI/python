class  BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
        
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.account = BankAccount(0.02, 0)


        def make_deposit(self, amount):
            self.account.deposit(amount)
            return self

        def make_withdrawal(self, amount):
            self.account.withdraw(amount)
            return self

        def display_user_balance(self):
            print(f"User: {self.name}, Balance: ${self.account.balance}")
            return self
    

account1 = BankAccount(0.01, 100)
account1.deposit(50).deposit(50).deposit(50).withdraw(30).yield_interest().display_account_info()
 
account2 = BankAccount(0.02, 200)
account2.deposit(100).deposit(50).withdraw(30).withdraw(20).withdraw(10).withdraw(5).yield_interest().display_account_info()

user1 = User("Dania", "dania@email.com")

user1.make_deposit(100).make_deposit(50).make_withdrawal(30).display_user_balance()