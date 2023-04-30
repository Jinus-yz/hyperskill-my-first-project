# Write your code here
products = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80,
}

print("Earned amount:")
total = 0

for product in products:
    product_sum = products[product]
    total += product_sum
    print(f"{product}: ${product_sum}")

print(f"Income: ${total}")

staff_expenses = int(input("Staff expenses: "))
other_expenses = int(input("Other expenses: "))
print(f"Net income: ${total - staff_expenses - other_expenses}")
