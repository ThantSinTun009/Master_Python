# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
        
#     # method
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposit {amount} Successfully")
        
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdraw {amount} Successfully")
#         else:
#             print("Insufficient Balance!")
        
#     def show_balance(self):
#         print(f"Current Balance: {self.balance}")
        
# account1 = BankAccount("John", 1000)
# account1.deposit(500)

# account1.show_balance()

# account1.withdraw(300)
# account1.show_balance()


# # test
# account1.withdraw(5000)

############# Exercise 3: Wallet class
# Attributes : owner, balance
# methods: add_money, spent_money, check_balance


class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def add_money(self, amount):
        self.balance += amount
        print(f"Money {amount} is added")
        
    def spend_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Money {amount} is spent!")
        else:
            print("Insufficient Amount in the Wallet!!")
        
    def check_balance(self):
        print(f"Current Balance : {self.balance}")

wallet1 = Wallet('Thant', 10000)
wallet1.check_balance()

wallet1.add_money(5000)
wallet1.check_balance()

wallet1.spend_money(3000)
wallet1.check_balance()


