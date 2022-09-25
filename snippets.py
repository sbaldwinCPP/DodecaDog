# %% imports

# file stuff
import os
import tkinter as tk
from tkinter import filedialog as fd



# %% file dialogs
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


# %% scatter plots
# plotting stuff
import matplotlib.pyplot as plt
import matplotlib as mpl

def QuickScatter(x, y, c, cmap=mpl.cm.cool, cmin=0, cmax=1):
        fig, ax = plt.subplots()

        norm = mpl.colors.Normalize(vmin=cmin, vmax=cmax)
        sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)

        ax.scatter(x, y, color=sm.cmap(sm.norm(c)))

        txt = [str(round(i,2)) for i in c]
        for i,j,k in zip(x,y,txt):
                ax.annotate(k, xy=(i, j))

        cb = plt.colorbar(sm,
                orientation='vertical',
                #label='Some Units',
                #labelpad=-40,
                )

        cb.set_label('Some Units', labelpad=-100)

        return fig, ax


# %%
### END