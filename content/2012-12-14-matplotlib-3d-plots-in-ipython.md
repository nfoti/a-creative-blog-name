Title: Matplotlib 3D plots in IPython
Date: 2012-12-14 10:13
Category: Python 
Tags: matplotlib, ipython
Slug: matplotlib-3d-plots-in-ipython
Author: Nick Foti

###Summary:

Assume that
``` python
import matplotlib.pyplot as plt
```
has been executed.

When using `mplot3d` in IPython you have to manually draw the axes 
which can be done using the `plt.draw` function (or `plt.plot([],[])`).  
For some reason the axes are not automatically drawn as with 2d plots.

###The full story:

IPython provides some nice functionality for interactive plotting.  For 
instance, the code
``` python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
```
pops up a figure with the graph of the `sin`
function over the interval $[0,2\pi]$.

When using `mplot3d` for 3d plots in IPython the constructed axes are
not drawn by default.  For instance the code (taken from the `mplot3d` 
examples)
``` python
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100
for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zl, zh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
```
results in a blank figure on the screen.  In order to see the results one
must manually draw the axes which can be done with the `plt.draw` function
(or with `plt.plot([],[])`).  I have no idea why this is the case, but 
hopefully it will be fixed at some point.
