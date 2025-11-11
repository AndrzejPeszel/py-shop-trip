class Car:
    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption  # liters per 100 km

    def fuel_cost(self, distance_km, fuel_price):
        return (distance_km * self.fuel_consumption / 100) * fuel_price
