def main():
    from customer import Customer
    from coffee import Coffee

    customer1 = Customer("Bakari")
    customer2 = Customer("Isaac")
    customer3 = Customer("John")
    customer4 = Customer("Kizito")

    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    coffee3 = Coffee("Drip Coffee")

    customer1.create_order(coffee1, 4.5)
    customer1.create_order(coffee2, 5.0)
    customer2.create_order(coffee1, 4.0)
    customer4.create_order(coffee3, 6.0)
    customer3.create_order(coffee3, 9.0)

    print("Coffees ordered by Bakari:", [c.name for c in customer1.coffees()])
    print("Customers who ordered Latte:", [c.name for c in coffee1.customers()])
    print("Latte total orders:", coffee1.num_orders())
    print("Latte average price:", coffee1.average_price())

    aficionado = Customer.most_aficionado(coffee3)
    if aficionado:
        print(f"Most aficionado of {coffee3.name}: {aficionado.name}")
    else:
        print(f"No aficionado found for {coffee3.name}")

if __name__ == "__main__":
    main()
