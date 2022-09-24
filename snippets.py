# %% 
# imports
import os
import tkinter as tk
from tkinter import filedialog as fd

# %% 
# file dialogs
def FileFolderDialog(method='single', 
        ftypes=[], 
        IncludeAllFiles=True,
        initdir=os.getcwd(),
        ):

    # add option for all files
    if IncludeAllFiles: ftypes.append(('All files', '*'))

    # create the root window
    root = tk.Tk()
    root.withdraw() # hides root window
    
    try:
        if method.lower() == 'single': 
                filename = fd.askopenfilename(
                        parent=root,
                        title='Select a file',
                        initialdir=initdir,
                        filetypes=ftypes,
                        )
        elif method.lower() == 'multi': 
                filename = fd.askopenfilenames(
                        parent=root,
                        title='Select file(s)',
                        initialdir=initdir,
                        filetypes=ftypes,
                        )
        elif method.lower() == 'folder': 
                filename = fd.askdirectory(
                        parent=root,
                        title='Select a folder',
                        initialdir=initdir,
                        )
        else: raise TypeError('method not recognized')
        return filename

    finally:
        root.destroy()
# %%
### END