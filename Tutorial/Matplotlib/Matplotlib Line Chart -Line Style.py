# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 1000)  


plt.figure(figsize=(4, 3))
plt.tight_layout()

for index, line_style in enumerate(['-', '--', ':', '-.']):
    y = np.sin(x - index*np.pi/2)
    plt.plot(x, y, 'k', linestyle=line_style, lw=2)

plt.title("Line Style")
plt.grid(True)
import os
plt.savefig(os.path.join(r"C:\Git\DelftStack\static\img\Matplotlib", 
                         os.path.basename(__file__).replace('py', 'png')))

plt.show()