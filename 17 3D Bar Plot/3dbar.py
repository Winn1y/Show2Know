import matplotlib
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  


x = np.arange(1, 6) 
y = np.arange(1, 4)  
x, y = np.meshgrid(x, y)  
z = np.random.randint(1, 10, size=x.shape)  
# Plotting the 3D bar chart
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Flattening arrays to pass them as parameters
x_flat = x.flatten()
y_flat = y.flatten()
z_flat = np.zeros_like(x_flat)  # Bottom of the bars
dz_flat = z.flatten()  # Heights of the bars

# Plotting bars
ax.bar3d(x_flat, y_flat, z_flat, dx=0.5, dy=0.5, dz=dz_flat)

# Labeling axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()