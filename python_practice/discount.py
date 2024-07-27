def calculate_discount(quantity, price):
    price_tot = quantity * price
    if price_tot >= 15:
        discount = ((price_tot - 15) * 0.2) + price_tot
        return discount
    else:
        return price_tot


x = int(input("Enter quantity: "))
y = int(input("Enter price: "))
print(calculate_discount(x, y))
