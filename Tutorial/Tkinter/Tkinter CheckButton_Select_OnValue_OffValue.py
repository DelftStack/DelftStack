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

chkValue = tk.StringVar() 
 
chkExample = tk.Checkbutton(app, text='Check Box', var=chkValue,
                            onvalue="RGB", offvalue="YCbCr") 
chkExample.grid(column=0, row=0)

chkExample.select()
print "The checkbutton value when selected is {}".format(chkValue.get())
chkExample.deselect()
print "The checkbutton value when deselected is {}".format(chkValue.get())

app.mainloop()
