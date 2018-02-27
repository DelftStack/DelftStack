#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
URL: https://www.delftstack.com/tutorial/tkinter-tutorial/tkinter-button/
Website: https://www.delftstack.com
"""

from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk
    
app = tk.Tk()
button1 = tk.Button(app, text="Python Label 1")
button2 = tk.Button(app, text="Python Label 2")
import pprint
pprint.pprint(dict(button1))
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
app.mainloop()