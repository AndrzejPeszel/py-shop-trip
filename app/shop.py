from datetime import datetime

class Shop:
    def __init__(self, name: str, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, cart: dict) -> float:
        total = 0
        for item, quantity in cart.items():
            if item in self.products:
                total += self.products[item] * quantity
        return total

    def print_receipt(self, customer_name: str, cart: dict, timestamp: datetime = None) -> float:
        if timestamp is None:
            timestamp = datetime.now()

        print(f"\nDate: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0
        for item, quantity in cart.items():
            unit_price = self.products[item]
            price = unit_price * quantity
            print(f"{quantity} x {item} @ ${unit_price:.2f} = ${price:.2f}")
            total += price
        print(f"Total cost is {total:.2f} dollars")
        print("See you again!")

        return total
