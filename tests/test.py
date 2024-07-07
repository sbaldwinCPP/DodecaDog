import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))

import dodecadog as dd


dd.gui.basic()
# dd.core.dpg_demo()

# print(dd.tk_tools.file_browse())
