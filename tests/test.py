import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))

import dodecadog as dd

dd.main.main()
