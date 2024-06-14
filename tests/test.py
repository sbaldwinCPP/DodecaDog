import sys
import os.path as path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import dodecadog as dd

dd.core.test()
dd.core.dpg_demo()
