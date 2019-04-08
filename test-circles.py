import circlify as circ
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import random

data = [19, 17, 13, 11, 7, 5, 3, 2, 1]
ccircles = circ.circlify(data, with_enclosure=True)

fig, ax = plt.subplots()

circles = []
for c in ccircles:
    circles.append( Circle((c.x, c.y), c.r) )

for c in circles:
    ax.add_artist(c)
    c.set_alpha(random.random())
    c.set_clip_box(ax.bbox)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

plt.show()
