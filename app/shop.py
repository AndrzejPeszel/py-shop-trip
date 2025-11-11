from datetime import datetime

class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def can_fulfill(self, product_cart):
        return all(product in self.products for product in product_cart)

    def calculate_product_cost(self, product_cart):
        return sum(self.products[product] * quantity for product, quantity in product_cart.items())

    def print_receipt(self, customer_name, product_cart):
        print(f"\nDate: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, quantity in product_cart.items():
            price = self.products[product] * quantity
            print(f"{quantity} {product}s for {price:.2f} dollars")
            total += price
        print(f"Total cost is {total:.2f} dollars")
        print("See you again!")
        return total
