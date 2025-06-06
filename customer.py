
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
    def name(self,value):
        # checks if name is a string and between 1 to 15 xters
        if not isinstance(value,str):
            raise ValueError('Name must be a string.')
        if not 1<=len(value)<=15:
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name= value

    def orders(self):
        from order import Order
        return([order for order in Order.all if order.customer==self]) 
     
    def coffees(self):
        # returns a set so duplicates then a list 
        return list({order.coffee for order in self.orders()})
    
    def create_order(self,coffee,price):
        from order import Order
        return Order(self,coffee,price)
    
    @classmethod
    def most_aficionado(cls,coffee):
        from order import Order
        # get customer from current order
        customer_spending={}
        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer,0) + order.price
        if not customer_spending:
            return None
        return max(customer_spending,key=customer_spending.get)    

if __name__ == "__main__":
    from coffee import Coffee  
    customer = Customer('Isaac')
    coffee = Coffee('cappuccino')
    customer.create_order(coffee, 4.50)
    print(customer.orders())

