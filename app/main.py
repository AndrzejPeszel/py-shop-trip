import json
from app.customer import Customer
from app.shop import Shop

def shop_trip():
    with open("app/config.json") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(**cust) for cust in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"\n{customer.name} has {customer.money} dollars")
        shop_costs = []
        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {cost:.2f}")
            shop_costs.append((shop, cost))

        affordable = [(shop, cost) for shop, cost in shop_costs if cost <= customer.money]
        if not affordable:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
            continue

        best_shop = min(affordable, key=lambda x: x[1])[0]
        customer.purchase(best_shop, fuel_price)
