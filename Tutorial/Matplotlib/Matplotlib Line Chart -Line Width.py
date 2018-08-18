# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 21)  


plt.figure(figsize=(4, 4))
plt.tight_layout()

for line_width in [0.5, 1, 2, 4, 8]:
    y = line_width * x
    plt.plot(x, y, 'k', linewidth=line_width)

plt.title("Line Width")
plt.grid(True)

plt.xlim([0, 20])
plt.ylim([0, 20])
import os
plt.savefig(os.path.join(r"C:\Git\DelftStack\static\img\Matplotlib", 
                         os.path.basename(__file__).replace('py', 'png')))

plt.show()