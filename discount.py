import datetime
today = datetime.datetime.now()
dow = today.weekday()
discount_rate = .1
tax_rate = .06
subtotal = 0
quantity = 1

while quantity != 0:
    quantity = int(input("\nEnter the quantity: "))
    if quantity != 0:
        price = float(input("Enter the price: "))
        subtotal += price * quantity

print(f"\nTotal order: ${subtotal:.2f}")
discount = 0

if dow == 2 or dow == 3:
    if subtotal >= 50:
        discount = subtotal * discount_rate
        print(f"Discount: ${discount:.2f}")

    elif subtotal < 50:
        short = 50 - subtotal

        print(
            f"\nNo discount available. You need to spend ${short:.2f} more "
            f" to qualify for the discount."
        )

subtotal -= discount        
tax = subtotal * tax_rate
total = subtotal + tax

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Due: ${total:.2f}\n")
