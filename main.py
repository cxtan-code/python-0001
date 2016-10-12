#!/bin/python

__author__ = "cxtan"
import random
my_dict = {}
def generete_activecode():
    for num in range(0, 200):
        random_num = int(random.random() * 1000000000)
        my_dict.setdefault(num, random_num)



if __name__ == '__main__':
    generete_activecode()
    pass





































