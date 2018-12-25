# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 01:50:56 2018

@author: Vaibhav"""
from sklearn import datasets
price_of_house=datasets.load_boston()
print(price_of_house.data)
digits=datasets.load_digits()
print(digits.images(4))
