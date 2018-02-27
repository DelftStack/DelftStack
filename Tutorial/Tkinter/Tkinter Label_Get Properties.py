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
    
from pprint import pprint
    
app = tk.Tk()
labelExample = tk.Label(app, text="This is a Label", height=15, width=100)
pprint(dict(labelExample))