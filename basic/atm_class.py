class Account:

    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def credit(self,amount_to_credited):
        self.amount_to_credited = amount_to_credited
        self.balance = self.balance + self.amount_to_credited
        return self.balance

    def debit(self,amount_to_debited):
        self.amount_to_debited = amount_to_debited
        if self.balance >= self.amount_to_debited:
            self.balance = self.balance - self.amount_to_debited
            return self.balance
        else:
            print("BALANCE NOT SUFFICIENT")

    def show_balance(self):
        return self.balance

account1 = Account(10000,260310413484)
while True:
    print("SELECT THE FOLLOWING OPTION")
    print("1. DEPOSIT\n2. WITHDRAW \n3. CHECK BALANCE\n4.EXIT")
    a = int(input("ENTER OPTION : "))
    if a==1:
        credit = int(input("AMOUNT TO BE CREDITED  :  "))
        if credit>0:
            account1.credit(credit)
        else:
            print("crediting amount must be positive")

    elif a==2:
        debit = int(input("AMOUNT TO BE DEBITED  :  "))
        account1.debit(debit)

    elif a==3:
        print(f"YOUR BALANCE IS {account1.show_balance()}")

    else :
        break
