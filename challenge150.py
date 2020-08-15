"""Given a list of points, a central point, and an integer k,
 find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], 
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)]."""

def k_nearest_points(points: list, center: tuple, k: int):
    points.sort(key = lambda x: ((x[0]**2 - center[0]**2) + (x[1]**2 - center[1]**2)))
    return points[:k]

if __name__ == "__main__":
    assert k_nearest_points([(0, 0), (5, 4), (3, 1)], (1, 2), 2) == [(0, 0), (3, 1)]
    
    
        