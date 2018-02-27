#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
Tutorial URL: https://www.delftstack.com/tutorial/tkinter-tutorial/hello-world/
Website: https://www.delftstack.com
"""
from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk
    
app = tk.Tk()
app.title("Hello World")
app.mainloop()
