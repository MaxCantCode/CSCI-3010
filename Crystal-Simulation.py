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

# if False:
if True:  # toggle for giant demo
    # giant cells
    points = np.array([[0, 0],
                       [0, 1],
                       [0, 1 / 2],
                       [1, -0.4],
                       [-1, 0]])
    voronoi_plot_2d(Voronoi(points))
    plt.title('giant cells\n{}'.format(voronoi_volumes(points)))
    plt.show()

    # normal example
    points = np.array([[0, 0],
                       [0, 1],
                       [0, 1 / 2],
                       [1, 0],
                       [-1, 0]])
    voronoi_plot_2d(Voronoi(points))
    plt.title('normal example\n{}'.format(voronoi_volumes(points)))
    plt.show()

np.random.seed(370)
# num_pts = 10 ** 5
num_pts = 10 ** 2 // 2
# num_pts = 15
points = np.random.rand(num_pts, 2)

volumes_ = np.sort(voronoi_volumes(points))

# filter out inf cells
v_no_inf = volumes_[volumes_ != np.inf]

cum_no_inf = np.cumsum(v_no_inf)

num_biggr = np.count_nonzero(cum_no_inf > 1)

# want sum(volumes) close to 1
# look around above/below 1, choose whichever closer
crit_pts = cum_no_inf[-num_biggr - 1:-num_biggr + 2]

if True:  # for num_pts=15<20
    try:
        np.argmin(abs(crit_pts - 1))
    except ValueError as e:
        print(e)  # not many giants
        crit_pts = cum_no_inf[-num_biggr - 1:]

print(crit_pts,
      cum_no_inf[-num_biggr],
      abs(crit_pts - 1),
      'argmin: {}'.format(np.argmin(abs(crit_pts - 1))),
      'num of giant cells: {}'.format(num_biggr),
      sep='\n')

# ab1 means above/below 1
ab1 = np.argmin(abs(crit_pts - 1))
# volumes = v_no_inf[:-num_biggr + ab1]
volumes = v_no_inf if len(v_no_inf[:-num_biggr + ab1]) == 0 else v_no_inf[:-num_biggr + ab1]

print('vol sum before:', np.sum(v_no_inf))
print('vol sum after:', np.sum(volumes))

if True:
    plt.title('Volume of Each Cell (with giants)')
    plt.plot(volumes_, '+')
    plt.show()

    plt.title('Volume of Each Cell')
    plt.plot(volumes, '+')
    plt.show()

    plt.title('cumsum Volume of Each Cell')
    plt.plot(np.cumsum(volumes), '+')
    plt.show()

    plt.title('Hist of Volume Plot')
    plt.hist(volumes)
    plt.show()

    plt.title(r'$F_n(s)=\frac{{n(s)}}{{n(s_{{max}})}},n_{{cells}}={}$'.format(len(volumes)))
    plt.plot(volumes, np.linspace(0, 1, len(volumes)), '+')
    plt.show()
