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
labelExample = tk.Button(app, text="0")

def change_label_number():
    counter = int(str(labelExample['text']))
    counter += 1
    labelExample.config(text=str(counter))
    
buttonExample = tk.Button(app, text="Increase", width=30,
                          command=change_label_number)

buttonExample.pack()
labelExample.pack()
app.mainloop()