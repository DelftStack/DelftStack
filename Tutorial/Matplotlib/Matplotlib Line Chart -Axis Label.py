# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 1000)  
y = np.sin(x)

plt.figure(figsize=(4, 3))


plt.plot(x, y, "r")
plt.xlabel("Time (s)", 
           family='serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)

plt.ylabel("Value", 
           family='monospace', 
           color='b', 
           weight='bold', 
           size = 16,
           labelpad = 4)

plt.grid(True)
plt.tight_layout()
import os
plt.savefig(os.path.join(r"C:\Git\DelftStack\static\img\Matplotlib", 
                         os.path.basename(__file__).replace('py', 'png')),
            dpi = 100)

plt.show()