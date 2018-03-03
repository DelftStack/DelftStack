#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
URL: https://www.delftstack.com/tutorial/python-3-basic-tutorial/namescape-and-scope/
Website: https://www.delftstack.com
"""

x = 1
y = 2
stringX = "String X"

def globalTest():
    for (key, value) in globals().items():
        print("{} - {}".format(key, value))
    
globalTest()