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
app.geometry('300x200')

buttonW = tk.Button(app, text="West")
buttonW.pack(side='left', ipadx=20, padx=30)

buttonE = tk.Button(app, text="East")
buttonE.pack(side='right', ipadx=20, padx=30)

app.mainloop()