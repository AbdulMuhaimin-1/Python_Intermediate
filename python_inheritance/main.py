#!/usr/bin/env python
# coding: utf-8

# # Inheritance Exercise Clothing
#
# The following code contains a Clothing parent class and two children classes: Shirt and Pants.
#
# Your job is to code a class called Blouse. Read through the code and fill out the TODOs. Then check your work with the unit tests at the bottom of the code.

# In[ ]:
import unittest

class Clothing:

    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

    def calculate_shipping(self, weight:float, rate:float):
        self.weight = weight
        self.rate = rate
        return weight * rate


class Shirt(Clothing):

    def __init__(self, color, size, style, price, long_or_short):
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2 * self.price


class Pants(Clothing):

    def __init__(self, color, size, style, price, waist):
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)


# TODO: Write a class called Blouse, that inherits from the Clothing class
class Blouse(Clothing):
    # and has the the following attributes and methods:
    #   attributes: color, size, style, price, country_of_origin
    def __int__(self, color, size, style, price, country_of_origin: str):
        Clothing.__init__(self, color, size, style, price)
        self.country = country_of_origin
#     where country_of_origin is a string that holds the name of a
#     country
#   methods: triple_price, which has no inputs and returns three times
#     the price of the blouse
    def triple_price(self):
        return self.price * 3
#

# TODO: Add a method to the clothing class called calculate_shipping.
#   The method has two inputs: weight and rate. Weight is a float
#   representing the weight of the article of clothing. Rate is a float
#   representing the shipping weight. The method returns weight * rate


# Write a test case to check your solution
class TestBlouse(unittest.TestCase):
    def test_blouse(self):
        blouse = Blouse('blue', 'medium', 'T-shirt', 25)
        self.assertEqual(blouse.triple_price(), 75, None)


if __name__ == '__main__':
    unittest.main()