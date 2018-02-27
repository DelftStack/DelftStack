#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
Website: https://www.delftstack.com
"""

import tkinter as tk


def callbackFunc():
    resultString.set("{} - {}".format(landString.get(),
                                      cityString.get()))
     
app = tk.Tk() 
app.geometry('200x100')

labelLand = tk.Label(app,
                    text = "Country")
labelLand.grid(column=0, row=0, sticky=tk.W)
labelCity = tk.Label(app,
                    text = "City")
labelCity.grid(column=0, row=1, sticky=tk.W)


landString = tk.StringVar()
cityString = tk.StringVar()
entryLand = tk.Entry(app, width=20, textvariable=landString)
entryCity = tk.Entry(app, width=20, textvariable=cityString)


entryLand.grid(column=1, row=0, padx=10)
entryCity.grid(column=1, row=1, padx=10)


resultButton = tk.Button(app, text = 'Get Result',
                         command=callbackFunc)

resultButton.grid(column=0, row=2, pady=10, sticky=tk.W)

resultString=tk.StringVar()
resultLabel = tk.Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=2, padx=10, sticky=tk.W)

app.mainloop()
