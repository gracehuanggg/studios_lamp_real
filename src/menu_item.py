class MenuItem:
    def __init__(self, id,name,category,price,in_stock=True,):
        self.id = int(id)
        self.name = name
        self.category = category
        self.price = float(price)
        self.in_stock = bool(in_stock)


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category":self.category,
            "price": self.price,
            "in_stock": self.in_stock,
        }

    @classmethod
    def from_dict(cls, data_dict):

        return cls(
            id=data_dict['id'],
            name=data_dict['name'],
            category=data_dict['category'],
            price=data_dict['price'],
            in_stock=data_dict.get('in_stock', True)
        )


