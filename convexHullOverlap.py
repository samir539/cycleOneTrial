
import scipy.spatial as scipy


def in_hull(p, hull):
  
    from scipy.spatial import Delaunay
    if not isinstance(hull,Delaunay):
        hull = Delaunay(hull)

    return hull.find_simplex(p)>=0