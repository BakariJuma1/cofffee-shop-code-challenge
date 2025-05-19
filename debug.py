from lib.customer import Customer
from lib.coffee import Coffee

customer1 = Customer("Bakari")
customer2 = Customer("Isaac")
customer3 =Customer('John')
customer4 = Customer('kizito')

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")
coffee3=Coffee('Drip coffee')

customer1.create_order(coffee1, 4.5)
customer1.create_order(coffee2, 5.0)
customer2.create_order(coffee1, 4.0)
customer4.create_order(coffee3,6.0)
customer3.create_order(coffee3,9.0)

print("----------------------------------------------------------------")

print("Coffees ordered by Bakari:", [c.name for c in customer1.coffees()])
print("Customers who ordered Latte:", [c.name for c in coffee1.customers()])
print("Latte total orders:", coffee1.num_orders())
print("Latte average price:", coffee1.average_price())

print("-----------------------------------------------------------------")

print('\n ---Orders by customer---')
for order in customer4.orders():
    print(f"Customer:{order.customer.name},coffee:{order.coffee.name},price:${order.price:.2f}")
for order in customer2.orders():
    print(f"Customer:{order.customer.name},coffee:{order.coffee.name},price:${order.price:.2f}")    
for order in customer1.orders():
    print(f"Customer:{order.customer.name},coffee:{order.coffee.name},price:${order.price:.2f}")      
for order in customer3.orders():
    print(f"Customer:{order.customer.name},coffee:{order.coffee.name},price:${order.price:.2f}")      

print('-----------------------------------------------------------------------------------------------')

aficionado = Customer.most_aficionado(coffee3)
if aficionado:
    print(f"\nMost aficionado of {coffee1.name} is {aficionado.name}")
else:
    print(f"\nNo aficionado found for {coffee1.name}")