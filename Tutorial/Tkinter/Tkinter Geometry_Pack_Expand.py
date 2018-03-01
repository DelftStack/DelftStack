#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
URL: https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-geometry-managers/
Website: https://www.delftstack.com
"""

import tkinter as tk
import calendar    
    
app = tk.Tk()
app.geometry('200x300')

buttonX = tk.Button(app, text="Label ", bg="blue", height=5)
buttonX.pack(fill='x')

listboxA = tk.Listbox(app, width=10)
listboxA.pack(fill='both', expand=0)

for i in range(1,13):
    listboxA.insert(tk.END, calendar.month_name[i])
    
app.mainloop()