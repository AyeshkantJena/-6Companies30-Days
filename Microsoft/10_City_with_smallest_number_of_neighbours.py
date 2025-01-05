class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        # Initialize the distance matrix with infinity
        distances = [[float('inf')] * n for _ in range(n)]
        
        # Distance from a city to itself is 0
        for i in range(n):
            distances[i][i] = 0
        
        # Filling the initial distances based on the edges
        for u, v, w in edges:
            distances[u][v] = w
            distances[v][u] = w
        
        # Using Floyd-Warshall algorithm to compute shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
        
        # Find the city with the smallest number of reachable cities within the threshold
        min_reachable = float('inf')
        result_city = -1

        for i in range(n):
            reachable = sum(1 for j in range(n) if distances[i][j] <= distanceThreshold)
            # Update the result city based on the problem's criteria
            if reachable < min_reachable or (reachable == min_reachable and i > result_city):
                min_reachable = reachable
                result_city = i

        return result_city
