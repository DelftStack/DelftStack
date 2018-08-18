# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 1000)  
y = np.sin(x)

plt.figure(figsize=(4, 3))
plt.tight_layout()

plt.plot(x, y, "r--")
import os
plt.savefig(os.path.join(r"C:\Git\DelftStack\static\img\Matplotlib", 
                         os.path.basename(__file__).replace('py', 'png')))

plt.show()