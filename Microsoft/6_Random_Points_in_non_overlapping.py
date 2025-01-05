import random
from bisect import bisect_left

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.areas = []
        self.total = 0
        
        # Precompute areas and store cumulative sum
        # Time complexity: O(n) where n is number of rectangles
        for x1, y1, x2, y2 in rects:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.total += area
            self.areas.append(self.total)
            
        # Store rectangle dimensions for O(1) access
        self.dimensions = [(x2-x1+1, y2-y1+1, x1, y1) 
                          for x1, y1, x2, y2 in rects]

    def pick(self):

        # Get random number and find corresponding rectangle
        target = random.random() * self.total
        idx = bisect_left(self.areas, target)
        
        # Get precomputed dimensions
        width, height, x1, y1 = self.dimensions[idx]
        
        # Generate random point within the rectangle
        x = x1 + random.randrange(width)
        y = y1 + random.randrange(height)
        
        return [x, y]
