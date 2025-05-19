class Order:
    # class variable that tracks the coffee
    all=[]
    
    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
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

        