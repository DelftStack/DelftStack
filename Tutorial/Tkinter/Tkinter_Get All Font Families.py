from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

import tkFont
from pprint import pprint

app = tk.Tk()
pprint(tkFont.families())  