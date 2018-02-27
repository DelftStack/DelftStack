#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
Website: https://www.delftstack.com
"""

import tkinter as tk
 
app = tk.Tk() 
app.geometry('150x100')

radioValue = tk.IntVar() 

 
rdioOne = tk.Radiobutton(app, text='January',
                             variable=radioValue, value=1) 
rdioTwo = tk.Radiobutton(app, text='Febuary',
                             variable=radioValue, value=2) 
rdioThree = tk.Radiobutton(app, text='March',
                             variable=radioValue, value=3)

rdioOne.grid(column=0, row=0)
rdioTwo.grid(column=0, row=1)
rdioThree.grid(column=0, row=2)

app.mainloop()
