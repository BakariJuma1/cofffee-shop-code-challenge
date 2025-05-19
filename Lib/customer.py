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
        pass    