#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
URL: https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-label/
Website: https://www.delftstack.com
"""

from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

import tkFont    
app = tk.Tk()
labelExample1 = tk.Label(app, text="Customized Label 1", font=("Times", 20))
labelExample2 = tk.Label(app, text="Customized Label 2", 
                         font=("Times", 20, "italic"))

labelFont3 = tkFont.Font(family="Helvetica", size=20, weight=tkFont.BOLD,
                         underline=1, overstrike=1)
labelExample3 = tk.Label(app, text="Customized Label 3", 
                         font=labelFont3)
labelExample1.pack()
labelExample2.pack()
labelExample3.pack()
app.mainloop()