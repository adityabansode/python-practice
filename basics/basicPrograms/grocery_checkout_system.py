prices = {
    "apple":0.50,
    "banana": 0.30,
    "milk":1.20,
    "bread":3.50
}

item1 = input("Enter name of first item:").lower()
item1_qty = int(input(f"Enter the quantity of {item1}:"))

item2 = input("Enter name of 2nd item:").lower()
item2_qty = int(input(f"Enter the quantity of {item2}:"))

item3 = input("Enter name of 3rd item:").lower()
item3_qty = int(input(f"Enter the quantity of {item3}:"))

item1_price = prices.get(item1,0)
item2_price = prices.get(item2,0)
item3_price = prices.get(item3,0)

item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty

subtotal = item1_total + item2_total + item3_total
tax = subtotal * 0.085
total_bill = subtotal + tax

print("\n----Receipt----")

print(f"{item1.capitalize()}: {item1_qty} @ ${item1_price:.2f} each = ${item1_total:.2f}")
print(f"{item2.capitalize()}: {item2_qty} @ ${item1_price:.2f} each = ${item2_total:.2f}")
print(f"{item3.capitalize()}: {item3_qty} @ ${item1_price:.2f} each = ${item3_total:.2f}")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Amount: ${total_bill:.2f}")