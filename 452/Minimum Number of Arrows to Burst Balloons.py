class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if len(points) == 0:
            return 0
        
        count = 1
        points = sorted(points, key = lambda x: x[1])
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                count += 1
                end = points[i][1]
        return count