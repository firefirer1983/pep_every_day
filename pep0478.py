#! /usr/bin/env python

# PEP0478 purpose is to avoid multi inhenritence of meta classes
# Add 2 api: __init_subclass__ and __set_name__
#
# Why we use meta classes?
# 1. do some initialization after class creation
# 2. init class attribute or descriptor value
# 3. keeping the order in which class attributes were defined
class BarMeta(type):
    pass

class FooMeta(type):
    pass

class Bar(metaclass=BarMeta):
    pass

class Foo(metaclass=FooMeta):
    pass

class Test(Bar, Foo):
    pass

def main():
    t = Test()

if __name__ == "__main__":
    exit(main())
    
