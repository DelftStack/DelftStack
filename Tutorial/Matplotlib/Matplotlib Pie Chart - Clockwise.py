
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


x = np.array([15, 25, 30, 40])
label = ["France", "Germany", "Uk", "US"]

plt.figure(figsize=(4, 3))
plt.tight_layout()

plt.pie(x, labels=label, counterclock=False)
plt.title("Pseduo Distribution")


import os
plt.savefig(os.path.join(r"C:\Git\DelftStack\static\img\Matplotlib", 
                         os.path.basename(__file__).replace('py', 'png')))

plt.show()