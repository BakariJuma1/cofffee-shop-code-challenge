
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
            raise ValueError("Please enter a valid price.")
        if not 1.0<= value <= 10:
            raise ValueError("Please enter a valid price.")
        if  hasattr(self,'_price'):
            raise ValueError('Price is already set and cannot be changed.')
        self._price = value
    
    @property
    def customer(self):
        return(self._customer)
    
    @customer.setter
    def customer(self,value):
        from customer import Customer
        if not isinstance(value,Customer):
            raise ValueError("Please enter a valid price.")
        self._customer= value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Please enter a valid price.")
        self._coffee = value    


if __name__ == "__main__":
    from customer import Customer
    from coffee import Coffee

    customer = Customer('ALICE')
    coffee = Coffee('latte')
    order = Order(customer, coffee, 4.50)
