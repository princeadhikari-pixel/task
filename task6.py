name = input("Enter customer name: ")
price = float(input("Enter product price: "))
qty = int(input("Enter quantity: "))
member = input("Are you a member? (yes/no): ")
sub = price * qty
if sub >= 10000:
    discount = sub * 15 / 100
elif sub >= 5000:
    discount = sub * 10 / 100
elif sub >= 2000:
    discount = sub * 5 / 100
else:
    discount = 0
if member == "yes" and sub >= 5000:
    discount = discount + (sub * 5 / 100)
final = sub - discount
print(f"Customer name: {name}")
print(f"Subtotal: Rs. {sub}")
print(f"Discount: Rs. {discount}")
print(f"Final amount: Rs. {final}")