
from .order import Order
from .coffee import Coffee


class Customer:
    all =[]

    def __init__(self,name):
        self.name = name
        Customer.all.append(self)

    # gets the name 
    @property
    def name(self):
        return self._name 

    # sets the name  
    @name.setter
    def name(self,name):
        # checks if name is a string and between 1 to 15 xters
        if not isinstance(name,str):
            raise Exception('name must be a string ')
        if not 1<=len(name)<=15:
            raise Exception("Name must be between 1-15 charachters")
        self._name= name

    def orders(self):
        return([order for order in Order.all if order.customer==self])  
    def coffees(self):
        # returns a set so duplicates then a list 
        return list({order.coffee for order in self.orders()})
    def create_order(self,coffee,price):
        return Order(self,coffee,price)

# creating instances    
customer=Customer('Isaac')
coffee= Coffee('cappuccino')

customer.create_order(coffee,4.50)
# print(customer.orders())