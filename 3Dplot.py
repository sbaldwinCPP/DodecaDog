# for creating a responsive plot
#%matplotlib widget

# importing required libraries
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np 
# # creating 3d plot using matplotlib
# # in python

# creating figure
fig = plt.figure()
ax = plt.axes(projection='3d')

# Creating scatter dataset
z = np.random.randint(100, size =(50))/100
x = np.random.randint(100, size =(50))/20
y = np.random.randint(100, size =(50))/20

# Creating surface dataset
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)


# plots
ax.scatter(x, y, z, cmap=cm.hot)
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True,
                       alpha=.5)

# ax.plot_wireframe(X, Y, Z, color='k',
#                        antialiased=True,
#                        alpha=.2
#                        )

# setting title and labels
ax.set_title("3D plot")
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

# displaying the plot
plt.show()
