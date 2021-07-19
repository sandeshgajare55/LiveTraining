class Product:
    def __init__(self,p_id,p_name,p_price):
        self.p_id=p_id
        self.p_name=p_name
        self.p_price=p_price

    def __str__(self):
        return f'Prod id{self.p_id},Prod Name{self.p_name},Prod Price{self.p_price}'

p1=Product(101,'Pen',50)
p2=Product(102,'Pencil',10)
p3=Product(103,'A4',3)

list1=[p1,p2,p3]
dict1={p1,p2,p3}
d1={key.p_id:key.p_name for key in dict1}
print(d1)



'''list_id=[i.p_id for i in list1 ]
list_name=[i.p_name for i in list1]
list_price=[i.p_price for i in list1]
print(list_id)
print(list_name)
print(list_price)
'''
