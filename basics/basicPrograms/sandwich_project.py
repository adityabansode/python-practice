toppings = ["onion","lettuce","tomato","olives","peppers","cucumber"]
print("Available toppings:",toppings)

topping1=input("Enter 1st topping:")
topping2=input("Enter 2nd topping:")
topping3=input("Enter 3rd topping:")

price_of_sandwich = 5

sandwich_qty = int(input("Enter how many sandwiches needed:"))

subtotal = sandwich_qty* price_of_sandwich
tax = 0.18 * subtotal
total_bill = subtotal + tax

print("\n----Receipt----")

print(f"Sandwich: {sandwich_qty} @ ${price_of_sandwich:.2f} each = ${subtotal:.2f}")


print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Amount: ${total_bill:.2f}")