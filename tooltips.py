#%%
#import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021
df = pd.read_csv('data/world-happiness-report-2021.csv')
x_name = 'Healthy life expectancy'
y_name = 'Freedom to make life choices'
color_name = 'Logged GDP per capita'
tooltip_name = 'Country name'
cmap = 'jet'
x = df[x_name]
y = df[y_name]
c = df[color_name]
tt = df[tooltip_name].values
# print(df.head())

#%%
fig, ax = plt.subplots()
sc = ax.scatter(x,y, c=c, cmap=cmap)
ax.set_xlabel(x_name)
ax.set_ylabel(y_name)
cb = plt.colorbar(sc)
cb.set_label(color_name)
# by default the tooltip is displayed "onclick"
# we can change it by setting hover to True
cursor = mplcursors.cursor(sc, hover=True)
# by default the annotation displays the xy positions
# this is to change it to the countries name
@cursor.connect("add")
def on_add(sel):
    #print(sel.index)
    sel.annotation.set(text=tt[sel.index])

plt.show()
# %%
