class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
       
        # Find the closest point to the circle's center within the rectangle
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Calculate the distance from the circle's center to this closest point
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y

        # Check if the distance is less than or equal to the radius
        return distance_x**2 + distance_y**2 <= radius**2