#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
website: https://www.delftstack.com
"""

import tkinter as tk
 
app = tk.Tk() 
app.geometry('150x100')

radioValue = tk.IntVar() 

 
rdioOne = tk.Radiobutton(app, text='I am raised',
                             variable=radioValue, value=1,
                             indicatoron = 0,
                             width=20) 
rdioTwo = tk.Radiobutton(app, text='I am sunken',
                             variable=radioValue, value=2,
                             indicatoron = 0,
                             width=20) 

rdioOne.grid(column=0, row=0)
rdioTwo.grid(column=0, row=1)

app.mainloop()
