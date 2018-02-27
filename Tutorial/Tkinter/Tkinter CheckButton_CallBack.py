#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
Website: https://www.delftstack.com
"""

import tkinter as tk
from _cffi_backend import callback
 
def callBackFunc():
    print "Oh. I'm clicked"
    
app = tk.Tk() 
app.geometry('150x100')

chkValue = tk.BooleanVar() 
chkValue.set(True)
 
chkExample = tk.Checkbutton(app, text='Check Box', 
                            var=chkValue, command=callBackFunc) 

chkExample.grid(column=0, row=0)

app.mainloop()
