class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n_points = len(points)
        
        distances = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            distances.append(distance)

        sorted_dist_with_idx = sorted(enumerate(distances), key=lambda x: x[1])
        
        k_closest_points = []
        for i in range(k):
            point_idx = sorted_dist_with_idx[i][0]
            point = points[point_idx]
            k_closest_points.append(point)

        return k_closest_points


        