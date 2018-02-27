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

buttonW = tk.Button(app, text="West", width=15)
buttonW.pack(side='left')

buttonE = tk.Button(app, text="East", width=15)
buttonE.pack(side='right')

app.mainloop()