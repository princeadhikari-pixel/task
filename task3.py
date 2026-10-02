unit = int(input("Enter units used: "))
if unit <= 20:
    bill = unit * 5
elif unit <= 50:
    bill = (20 * 5) + ((unit - 20) * 7)
elif unit <= 100:
    bill = (20 * 5) + (30 * 7) + ((unit - 50) * 10)
else:
    bill = (20 * 5) + (30 * 7) + (50 * 10) + ((unit - 100) * 12)
print(f"Units consumed: {unit}")
print(f"Total bill: Rs. {bill}")