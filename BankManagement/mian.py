class BankAccount:
    pass





print("press 1 for create an account")
print("press 2 for deposit account ")
print("press 3 for withdraw ")
print("press 4 for details")
print("press 5 for update details")
print("press 6 for delete the account")

a = int(input("enter the chioce : "))
if a<1 and a>6:
    print("select appropriate choice")
    a = int(input("enter the chioce : "))
else:
    if a == 1:
        pass