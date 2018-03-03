#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
URL: https://www.delftstack.com/tutorial/python-3-basic-tutorial/namescape-and-scope/
Website: https://www.delftstack.com
"""
outer = 'global variable'

def searchOrderFunc():
	enclosing = 'enclosing variable'
	
	def searchOrderFuncInner():
		inner = 'inner variable'
		print(inner)           #fetch from (L)ocal scope
		print(enclosing)       #fetch from (E)nclosing scope
		print(outer)           #fetch from (G)lobal scope
		print(any)             #fetch from (B)uilt-ins
	
	searchOrderFuncInner()
    
searchOrderFunc()