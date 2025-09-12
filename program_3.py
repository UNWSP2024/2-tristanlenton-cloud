item1 = int(input("Item 1: "))
item2 = int(input("Item 2: "))
item3 = int(input("Item 3: "))
item4 = int(input("Item 4: "))
item5 = int(input("Item 5: "))
subtotal = (item1 + item2 + item3 + item4 + item5)
tax = (item1 + item2 + item3 + item4 + item5) * 0.07
print("Subtotal:", subtotal)
print("Tax:", tax)
total = subtotal + tax
print("Total:", total)
