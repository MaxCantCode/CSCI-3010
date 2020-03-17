import numpy as np
from scipy.spatial import Voronoi, ConvexHull, voronoi_plot_2d
import matplotlib.pyplot as plt


# from https://stackoverflow.com/questions/19634993
# also useful: https://stackoverflow.com/questions/20515554
def voronoi_volumes(points):
    v = Voronoi(points)
    vol = np.zeros(v.npoints)
    for i, reg_num in enumerate(v.point_region):
        indices = v.regions[reg_num]
        if -1 in indices:  # some regions can be opened
            vol[i] = np.inf
        else:
            vol[i] = ConvexHull(v.vertices[indices]).volume
    return vol


# giant cells
points = np.array([[0, 0],
                   [0, 2],
                   # [0, -2],
                   [2, 0],
                   [-2, 0],
                   [0, 1],
                   # [0, -1],
                   [1, 0 - 1 / 25],
                   [-1, 0]])
voronoi_plot_2d(Voronoi(points))
plt.title('giant cells\n{}'.format(voronoi_volumes(points)))
plt.show()

# normal example
points = np.array([[0, 0],
                   [0, 2],
                   [0, -2],
                   [2, 0],
                   [-2, 0],
                   [0, 1],
                   [0, -1],
                   [1, 0],
                   [-1, 0]])
voronoi_plot_2d(Voronoi(points))
plt.title('normal example\n{}'.format(voronoi_volumes(points)))
plt.show()

np.random.seed(370)
# num_pts = 10 ** 5
num_pts = 10 ** 2 // 2
points = np.random.rand(num_pts, 2)

volumes_ = np.sort(voronoi_volumes(points))

# filter out inf cells
v_no_inf = volumes_[volumes_ != np.inf]

cum_no_inf = np.cumsum(v_no_inf)

num_biggr = np.count_nonzero(cum_no_inf > 1)

# want sum(volumes) close to 1
# look around above/below 1, choose whichever closer
crit_pts = cum_no_inf[-num_biggr - 1:-num_biggr + 2]

print(crit_pts,
      cum_no_inf[-num_biggr],
      abs(crit_pts - 1),
      'argmin: {}'.format(np.argmin(abs(crit_pts - 1))),
      'num_biggr: {}'.format(num_biggr),
      sep='\n')

# ab1 means above/below 1
ab1 = np.argmin(abs(crit_pts - 1))
volumes = v_no_inf[:-num_biggr + ab1]
print(np.sum(v_no_inf))
print(np.sum(volumes))

plt.title('Area of Each Cell (with giants)')
plt.plot(volumes_, '+')
plt.show()

plt.title('Area of Each Cell')
plt.plot(volumes, '+')
plt.show()

plt.title('cumsum Area of Each Cell')
plt.plot(np.cumsum(volumes), '+')
plt.show()

plt.title('Hist of Area Plot')
plt.hist(volumes)
plt.show()
