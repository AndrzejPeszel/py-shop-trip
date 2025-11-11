import math
from app.car import Car
from app.shop import Shop

class Customer:
    def __init__(self, name, cart, location, money, car_info):
        self.name = name
        self.cart = cart
        self.location = location
        self.home = location[:]
        self.money = money
        self.car = Car(car_info["brand"], car_info["fuel_consumption"])

    def distance_to(self, other_location: list) -> float:
        return round(math.dist(self.location, other_location), 2)

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        fuel_to_shop = self.car.fuel_cost(distance, fuel_price)
        fuel_home = self.car.fuel_cost(distance, fuel_price)
        product_cost = shop.calculate_product_cost(self.cart)
        return round(fuel_to_shop + product_cost + fuel_home, 2)

    def can_afford(self, total_cost: float) -> bool:
        return self.money >= total_cost

    def go_to_shop(self, shop: Shop, fuel_price: float):
        print(f"{self.name} rides to {shop.name}")
        shop.print_receipt(self.name, self.cart)
        self.location = shop.location[:]
        self.money -= shop.calculate_product_cost(self.cart)

    def go_home(self, shop: Shop, fuel_price: float):
        distance = self.distance_to(self.home)
        fuel_home = self.car.fuel_cost(distance, fuel_price)
        self.money -= fuel_home
        self.location = self.home[:]
        print(f"\n{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars\n")
