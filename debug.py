from lib.customer import Customer
from lib.coffee import Coffee

c1 = Customer("Bakari")
c2 = Customer("Isaac")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 4.5)
c1.create_order(coffee2, 5.0)
c2.create_order(coffee1, 4.0)

print("Coffees ordered by Bakari:", [c.name for c in c1.coffees()])
print("Customers who ordered Latte:", [c.name for c in coffee1.customers()])
print("Latte total orders:", coffee1.num_orders())
print("Latte average price:", coffee1.average_price())
