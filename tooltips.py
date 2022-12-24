#%%
#import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib widget

# https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021
df = pd.read_csv('data/world-happiness-report-2021.csv')
#df = df[df['year'] == 2020]
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
# fig, ax = plt.subplots(1, figsize=(12,6))
# ax.scatter(x, y)
# plt.xlabel(x_name)
# plt.ylabel(y_name)

# annot_x = (plt.xlim()[1] + plt.xlim()[0])/2
# annot_y = (plt.ylim()[1] + plt.ylim()[0])/2
# txt = ax.text(annot_x, annot_y, "Chart Ready", 
#               ha='center', fontsize=36, color='#DD4012')
# def hover(event):
#     txt.set_text("")

# #fig.canvas.mpl_connect("motion_notify_event", hover)
# click = fig.canvas.mpl_connect("button_press_event", hover)

# plt.show()

# %%
# #plt.close('all')
# fig, ax = plt.subplots(1, figsize=(12,6))
# ax.scatter(x,y)
# plt.xlabel(x_name)
# plt.ylabel(y_name)
# lnx = plt.plot([60,60], [0,1.5], color='black', linewidth=0.3)
# lny = plt.plot([0,100], [1.5,1.5], color='black', linewidth=0.3)
# lnx[0].set_linestyle('None')
# lny[0].set_linestyle('None')
# plt.xlim(x.min()*0.95, x.max()*1.05)
# plt.ylim(y.min()*0.95, y.max()*1.05)

# def hover(event):
#     lnx[0].set_data([event.xdata, event.xdata], [0, 1.5])
#     lnx[0].set_linestyle('--')
#     lny[0].set_data([0,100], [event.ydata, event.ydata])
#     lny[0].set_linestyle('--')
    
# fig.canvas.mpl_connect("motion_notify_event", hover)
# plt.show()

#%%
# fig, ax = plt.subplots(1, figsize=(12,6))
# # plot and labels
# cmap = 'jet'
# sc = ax.scatter(x,y, c=c, cmap=cmap)
# plt.colorbar(sc)
# plt.xlabel(x_name)
# plt.ylabel(y_name)
# # cursor grid lines
# lnx = plt.plot([60,60], [0,1.5], color='black', linewidth=0.3)
# lny = plt.plot([0,100], [1.5,1.5], color='black', linewidth=0.3)
# lnx[0].set_linestyle('None')
# lny[0].set_linestyle('None')
# # annotation
# annot = ax.annotate("", xy=(0,0), xytext=(5,5),textcoords="offset points")
# annot.set_visible(False)
# # xy limits
# plt.xlim(x.min()*0.95, x.max()*1.05)
# plt.ylim(y.min()*0.95, y.max()*1.05)
# def hover(event):
#     # check if event was in the axis
#     if event.inaxes == ax:
#         # draw lines and make sure they're visible
#         lnx[0].set_data([event.xdata, event.xdata], [0, 1.5])
#         lnx[0].set_linestyle('--')
#         lny[0].set_data([0,100], [event.ydata, event.ydata])
#         lny[0].set_linestyle('--')
#         lnx[0].set_visible(True)
#         lny[0].set_visible(True)
        
#         # get the points contained in the event
#         cont, ind = sc.contains(event)
#         if cont:
#             # change annotation position
#             annot.xy = (event.xdata, event.ydata)
#             # write the name of every point contained in the event
#             annot.set_text("{}".format(', '.join([tt[n] for n in ind["ind"]])))
#             annot.set_visible(True)    
#         else:
#             annot.set_visible(False)
#     else:
#         lnx[0].set_visible(False)
#         lny[0].set_visible(False)
# fig.canvas.mpl_connect("motion_notify_event", hover)
# plt.show()

#%%
import matplotlib.pyplot as plt
import mplcursors
#%matplotlib widget
fig, ax = plt.subplots()
sc = ax.scatter(x,y, c=c, cmap=cmap)
cb = plt.colorbar(sc)
cb.set_label(color_name)
# by default the tooltip is displayed "onclick"
# we can change it by setting hover to True
cursor = mplcursors.cursor(sc, hover=True)
# by default the annotation displays the xy positions
# this is to change it to the countries name
@cursor.connect("add")
def on_add(sel):
    sel.annotation.set(text=tt[sel.target.index])
plt.show()
# %%
