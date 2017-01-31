#!/usr/bin/python

class Fruit(object):
    edible = True

def make_sweet(fruit_class):
    setattr(fruit_class, 'taste', 'sweet')

orange = Fruit()
make_sweet(orange)

print orange.taste
print orange.edible