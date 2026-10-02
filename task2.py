number = int(input("Enter an integer: "))
if number > 0:
    status = "Positive"
elif number < 0:
    status = "Negative"
else:
    status = "Zero"

if number % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"
divisible_by_3 = number % 3 == 0
divisible_by_5 = number % 5 == 0
divisible_by_both = number % 3 == 0 and number % 5 == 0
print(f"\nNumber: {number}")
print(f"Type: {status}")
print(f"Even/Odd: {even_odd}")
print(f"Divisible by 3: {divisible_by_3}")
print(f"Divisible by 5: {divisible_by_5}")
print(f"Divisible by both 3 and 5: {divisible_by_both}")