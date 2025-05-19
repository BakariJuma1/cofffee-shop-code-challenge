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
           
        