from .order import Order
class Coffee:
    all = []
    def __init__(self,name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return(self._name)

    @name.setter 
    def name(self,name):
        if not isinstance(name,str):
            raise Exception("namemust be a string")
        if len(name)<3:
            raise Exception('name must be atleast 3 charachters')
        # making the name immutable once a coffee name is setyou cant change 
        if hasattr(self,'_name'):
            raise Exception('Coffee name can not be changed ')
        self._name = name
           
    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders)/ len(orders)  