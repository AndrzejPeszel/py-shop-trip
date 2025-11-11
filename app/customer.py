import math
from app.car import Car

class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location[:]
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def distance_to(self, shop_location):
        return round(math.dist(self.location, shop_location), 2)

    def trip_cost(self, shop, fuel_price):
        if not shop.can_fulfill(self.product_cart):
            return float('inf')
        distance = self.distance_to(shop.location)
        fuel_to_shop = self.car.fuel_cost(distance, fuel_price)
        fuel_home = self.car.fuel_cost(distance, fuel_price)
        product_cost = shop.calculate_product_cost(self.product_cart)
        return round(fuel_to_shop + product_cost + fuel_home, 2)

    def go_to(self, location):
        self.location = location

    def go_home(self):
        self.location = self.home_location

    def purchase(self, shop, fuel_price):
        distance = self.distance_to(shop.location)
        fuel_total = self.car.fuel_cost(distance, fuel_price) * 2
        product_total = shop.calculate_product_cost(self.product_cart)
        total_cost = fuel_total + product_total

        print(f"{self.name} rides to {shop.name}")
        self.go_to(shop.location)
        shop.print_receipt(self.name, self.product_cart)
        self.go_home()
        self.money -= total_cost
        print(f"\n{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars")
