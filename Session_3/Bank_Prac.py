# class Bank:
#     def __init__(self, name, acc_num, balance):
#         self.name = name
#         self.acc_num = acc_num
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Rs. {amount} has be credited into the account. Current Balance Rs. {self.balance}")

#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"Rs. {amount} has be debited from the account. Current Balance Rs. {self.balance}")


# am1 = Bank("Jewel", 22011012015, 100000)
# am1.deposit(10000)


class Bank:
    def __init__(self, name, account, bal):
        self.name = name
        self.account = account
        self.bal = bal
    def deposit(self, amount):
        self.bal += amount # self.bal = self.bal + amount
        print(f"Rs. {amount} has been credited into the account. Current Balance Rs. {self.bal}") # f-string
    def withdraw(self, amount):
        self.bal -= amount
        print(f"Rs. {amount} has been debited from the account. Current Balance Rs. {self.bal}")

am1 = Bank("Jewel", 6564454, 1000)
am1.deposit(100)