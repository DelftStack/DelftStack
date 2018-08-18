#!/usr/bin
# -*- coding: utf-8 -*-
"""
DelftStack Python Tkinter Tutorial

Author: Jinku Hu
URL: https://www.delftstack.com/tutorial/Matplotlib/Introduction and Installation/
Website: https://www.delftstack.com
"""

from matplotlib import pyplot as plt

plt.figure(figsize=(4,3))
plt.tight_layout()

plt.plot([1,2,3], [4,5,6])


import os
plt.savefig(r"Matplot Hello World.png")
plt.show()

