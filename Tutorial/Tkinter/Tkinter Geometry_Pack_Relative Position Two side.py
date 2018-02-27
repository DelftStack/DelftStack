#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
URL: https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-geometry-managers/
Website: https://www.delftstack.com
"""

import tkinter as tk    
    
app = tk.Tk()
app.geometry('300x400')

buttonW = tk.Button(app, text="West", width=15)
buttonW.pack(side='left')

buttonE1 = tk.Button(app, text="East 1", width=15)
buttonE1.pack(side='right')

buttonE2 = tk.Button(app, text="East 2", width=15)
buttonE2.pack(side='right')


app.mainloop()