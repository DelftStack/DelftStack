#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
Website: https://www.delftstack.com
"""

import tkinter as tk

app = tk.Tk() 

labelWidth = tk.Label(app,
                    text = "Width Ratio")
labelWidth.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

labelHeight = tk.Label(app,
                    text = "Height Ratio")
labelHeight.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)


entryWidth = tk.Entry(app, width=20)
entryHeight = tk.Entry(app, width=20)

entryWidth.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N)
entryHeight.grid(column=1, row=1, padx=10, pady=5, sticky=tk.S)


resultButton = tk.Button(app, text = 'Get Result')
resultButton.grid(column=0, row=2, pady=10, sticky=tk.W)

logo = tk.PhotoImage(file='python.gif')
labelLogo = tk.Label(app, image=logo)

labelLogo.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)

app.mainloop()
