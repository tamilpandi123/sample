class BankAccount:
    def __init__(self, acc_name, initialAmount):
        self.name = acc_name
        self.balance = initialAmount
        print(
            f"Account '{self.name}' created\nBalance = Rs.{self.balance}"
        )
    def getBalance(self):
        print(f" {self.name} Yours Bank Balance is Rs.{self.balance} ")
    def deposit(self,depositAmount):
        self.balance+=depositAmount
        print(f"{self.name} Yours Deposited amount was added to yours Account . Now Your , Bank Balance :{self.balance}")
    def withdraw(self,depositAmount):
        if depositAmount==self.balance:
            print(f"Rs.{depositAmount} is Withdrawan . Now,  Yours New Bank Balance :Rs.{self.balance}")
        else:
            print(f"{self.name} . Your withdraw Amount is Insufficient Amount for withdrawn")

tamizh = BankAccount("tamizh",1000)
pandi = BankAccount("pandi",2000)
tamizh.getBalance()
tamizh.deposit(2000)
tamizh.withdraw(3001)
pandi.getBalance()
pandi.deposit(1000)
pandi.withdraw(2000)
