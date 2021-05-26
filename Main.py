items = ["Box", "Paper", "Pen"]

item_prices = []
item_qty = []
subtotal = 0
sale_tax = 0.088

for item in items:
    item_price = int(input("Please enter the prices: "))
    item_qty = int(input("Please enter the quantities: "))
    T = item_price * item_qty
    item_prices.append(T)

print(item_prices)

for price in item_prices:
    subtotal += price   #subtotal = subtotal + price

print(subtotal)

Total_sale_tax = subtotal * sale_tax
print(Total_sale_tax)

Total_amount = subtotal + Total_sale_tax
print(Total_amount)