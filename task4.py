balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
pin = input("Enter PIN: ")
if pin != "1234":
    print("Invalid PIN")
elif amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print(f"Withdrawal successful")
    print(f"Remaining balance: Rs. {balance}")