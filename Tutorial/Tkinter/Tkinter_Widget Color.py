#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
Website: https://www.delftstack.com
"""

from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

import tkFont    
app = tk.Tk()
labelExample1 = tk.Label(app, text="Customized Color", 
                         font=("Times", 20),
                         bg="gray", fg="red")

labelExample1.pack()

app.mainloop()