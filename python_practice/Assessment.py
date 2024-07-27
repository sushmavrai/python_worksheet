def calc_espresso_price(quantity):
    return quantity * 1.5


def calc_latte_price(quantity):
    return quantity * 3.25


def calc_cappuccino_price(quantity):
    return quantity * 2.75


def total_price(espresso_quantity, latte_quantity, cappuccino_quantity):
    espresso_price = calc_espresso_price(espresso_quantity)
    latte_price = calc_latte_price(latte_quantity)
    cappuccino_price = calc_cappuccino_price(cappuccino_quantity)
    price = espresso_price + latte_price + cappuccino_price
    print(f"{espresso_quantity} * Espresso($1.5)---{espresso_price}")
    print(f"{latte_quantity} * Latte($3.25)---{latte_price}")
    print(f"{cappuccino_quantity} * Cappuccino($2.75)---{cappuccino_price}")
    print(f"Total --- {price}")

def header():
    print("Developers Cafe")
    print("---------------")

header()
print(total_price(2, 3, 4))