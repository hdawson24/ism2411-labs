# Exercise 1: Build a list
print("--- Exercise 1: Build a list---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice---")
print(inventory[0]) # always grabs the first item
print(inventory[-1]) # always grabs the last item

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item


print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # grabs first three items
print(inventory[-2:]) # grabs last two items
print(inventory[::2]) # grabs every other item 

print("--- Exercise 4: List Methods ---")

inventory.append("envelope") # adds item to end of list
inventory.append("tape") # adds item to end of list
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort() # sorts list in alphabetical order
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) # New York City coordinates 

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")


print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}" )
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")


print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # an empty list
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply a 10 percent discount

print(prices)
print(discounted)

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = [] # an empty list

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"count: {len(high_sales)}")
print(f"Average: {sum(high_sales / len(high_sales):.2f}")