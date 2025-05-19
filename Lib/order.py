class Order:
    # class variable that tracks the coffee
    all=[]
    
    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return(self._price)

    @price.setter
    def price(self,price):
        if not isinstance(price,float):
            raise Exception("price must be a float ")
        if not 1.0<= price <= 10:
            raise Exception("price should be between 1.0 to 10")
        if not hasattr(self,'_price'):
            raise Exception('price can not be changed ')
        self._price = price

        