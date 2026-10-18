a = int(input("enter any number from 1 to 10 (1 and 10 included) : "))

try:
    if a > 10 or a <= 0:
        raise ValueError ("VALUE IS NOT FROM 1 TO 10")
except Exception as r:
    print(f"AN ERROR HAS OCCURED AS {r}")

else:
    print(f"number {a} is correct")

finally:
    print("completed")
