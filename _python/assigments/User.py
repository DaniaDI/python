class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount

    def make_deposit(self, amount):
        self.balance += amount

    def display_user_balance(self): 
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, friends, amount): # بدي احول لشخص مثلا 20 بتالي انا عند  الحساب  بنقص والشخص حيزيد
        self.balance -= amount
        friends.balance += amount
        print(f"User: {self.name} transfered ${amount} to {friends.name}. New balance: ${self.balance}  and friends balance: ${friends.balance}")


user1 = User("Dania", 100)
user1.make_deposit(50)
user1.make_withdrawal(20)
user1.display_user_balance()

 # بدي احول لشخص مثلا 20 بتالي انا عند  الحساب  بنقص والشخص حيزيد
user2 = User("Alaa", 200)
user2.make_deposit(60)
user2.make_withdrawal(30)
user2.display_user_balance()
user2.transfer_money(user1,100)

user3 = User("Aman", 300)
user3.make_deposit(70)
user3.make_withdrawal(30)
user3.display_user_balance()
user3.transfer_money(user1,100)

user1.transfer_money(user3, 50)## المطلوب