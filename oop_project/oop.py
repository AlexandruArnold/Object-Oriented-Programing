"""
    New oriented-object programming project
"""
from item import Item
from phone import Phone

Item.instantiate_from_csv()
item1 = Phone("Sony", 100, 2, 2)
item1.apply_increment(0.2)
print(item1.price)