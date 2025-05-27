
class Order:

    # tracking all order instannces every new order is automatically added
    all=[]
    
    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # adds to the tracking list of all
        Order.all.append(self) 
        print(f"Creating order with price: {price}") 

    @property
    def price(self):
        return(self._price)

    @price.setter
    def price(self,value):
        if not isinstance(value,float):
            raise Exception("price must be a float ")
        if not 1.0<= value <= 10:
            raise Exception("price should be between 1.0 to 10")
        if  hasattr(self,'_price'):
            raise Exception('price can not be changed after creation ')
        self._price = value
    
    @property
    def customer(self):
        return(self._customer)
    
    @customer.setter
    def customer(self,value):
        from customer import Customer
        if not isinstance(value,Customer):
            raise Exception("Must be a coffee instance")
        self._customer= value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise Exception("coffee must be a Coffee instance")
        self._coffee = value    


if __name__ == "__main__":
    from customer import Customer
    from coffee import Coffee

    customer = Customer('ALICE')
    coffee = Coffee('latte')
    order = Order(customer, coffee, 4.50)
