import json
import random
import string
from pathlib import Path

class BankAccount:
    data = []
    database = "C:\\self_practice\\BankManagement\\data.json"

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("path does not exist")

    except Exception as e:
        print(f"an exception as occured as {type(e).__name__} : {e}")

    @staticmethod
    def __accountnumber():
        a = random.choices(string.digits, k = 12)
        return str("".join(a))

    @classmethod
    def __update(cls):
        with open(BankAccount.database,"w") as fs:
            fs.write(json.dumps(BankAccount.data))

    def createacoount(self):
        try:
            info = {
                "name" : input("enter your name : ") ,
                "age" : int(input("enter your age : ")),
                "email_id" : input("enter your email id : "),
                "phone_number" : int(input("enter your phonr number :")),
                "pin" : int(input("enter a 4 digit pin : ")),
                "account_number" : BankAccount.__accountnumber(),
                "balance" : 0
        }
        except Exception as e:
            print(f"an exception as occured as {type(e).__name__} : {e}")

        else: 
            if info["age"] <18:
                print("account cannot be craeted as age is less than 18")

                
            else:
                while len(str(info["pin"])) != 4:
                    print("your pin is less than 4 digit")
                    info["pin"] = int(input("renter your 4 digit pin :"))
                
                print("your account is successfully created ")

                for i in info:
                    print(f"{i} : {info[i]}")

                BankAccount.data.append(info)
                BankAccount.__update()





while True:
    user = BankAccount()

    print("press 1 for create an account")
    print("press 2 for deposit account ")
    print("press 3 for withdraw ")
    print("press 4 for details")
    print("press 5 for update details")
    print("press 6 for delete the account")
    a = int(input("enter the chioce : "))
    while a<1 or a>6:
        a = int(input("enter the chioce : "))

    else:
        if a == 1:
            user.createacoount()