class Solution:
    def imageSmoother(self, img):
        rows, cols = len(img), len(img[0])
        # Create the result matrix with the same dimensions as the input
        result = [[0] * cols for _ in range(rows)]

        # Directions for traversing neighbors
        directions = [
            (-1, -1), (-1, 0), (-1, 1), 
            (0, -1),        (0, 1), 
            (1, -1), (1, 0), (1, 1)
        ]

        for i in range(rows):
            for j in range(cols):
                # Initialize sum and count
                total_sum = img[i][j]
                count = 1

                # Check all 8 neighbors
                for dr, dc in directions:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < rows and 0 <= nj < cols:
                        total_sum += img[ni][nj]
                        count += 1

                # Compute the average and store it in the result matrix
                result[i][j] = total_sum // count

        return result