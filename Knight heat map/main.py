import random
import numpy as np
import numpy.random
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
viridis = cm.get_cmap('plasma', 64)


coords = []

for x in range(1,9):
    for y in range(1,9):
        coords.append([str(x),str(y)])
#print(coords)
points = {}
for i in coords:
    points[int("".join(i))] = 0
#print(points)
jumps = {}

for i in points:
    jumps[i] = [i+n for n in [-21,-19,-12,-8,8,12,19,21] if (i+n in points)]
#print(jumps)

positions = []
position = 17
for i in range(999999):
    points[position] +=1
    #print(position)
    positions.append(str(position))
    position = random.choice(jumps[position])
#print(points)
    
#print(positions)
x = []
y = []
for i in positions:
    x.append(int(i[0]))
    y.append(int(i[1]))
# Create data
#x = np.random.randn(9999)
#y = np.random.randn(9999)

# Create heatmap
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(8,8))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
#print(xedges)
#print(yedges)
# Plot heatmap
plt.clf()
plt.ylabel('y')
plt.xlabel('x')
plt.imshow(heatmap, extent=extent, cmap=viridis)
plt.show()

    
