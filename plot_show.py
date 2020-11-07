from numpy import arange, array
import shapefile
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.pyplot import get_cmap

shpFilePath = "RF/admin_4"
sf = shapefile.Reader(shpFilePath)

recs = sf.records()
shapes = sf.shapes()

cns = []
Nshp = len(shapes)

for nshp in range(Nshp):
    cns.append(recs[nshp][1])

cns = array(cns)
cm    = get_cmap('magma')
cccol = cm(1.*arange(Nshp)/Nshp)

fig = plt.figure()
ax = fig.add_subplot(111)

for nshp in range(Nshp):
    ptchs = []

    pts = array(shapes[nshp].points)
    prt = shapes[nshp].parts
    par = list(prt) + [pts.shape[0]]

    for pij in range(len(prt)):
        ptchs.append(Polygon(pts[par[pij]:par[pij+1]], lw=0))

    ax.add_collection(PatchCollection(ptchs, facecolor=cccol[nshp, :], edgecolor='k', linewidths=0, label="some"))

ax.set_xlim(10, 200)
ax.set_ylim(35, 90)

fig.set_size_inches(16, 8)

plt.axis('off'), plt.xticks([]), plt.yticks([]), plt.gca().axes.get_yaxis().set_visible(False)

plt.show()
