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

chkValue = tk.BooleanVar() 
chkValue.set(True)
 
chkExample = tk.Checkbutton(app, text='Check Box', var=chkValue) 
chkExample.grid(column=0, row=0)

chkExample.select()
print "The checkbutton value when selected is {}".format(chkValue.get())
chkExample.select()
print "The checkbutton value when deselected is {}".format(chkValue.get())

app.mainloop()
