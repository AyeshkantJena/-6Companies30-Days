from collections import defaultdict

class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        # Edge case: If lengths of source and target do not match
        if len(source) != len(target):
            return -1
        
        # Build a mapping of transformation costs
        transform_cost = defaultdict(lambda: float('inf'))
        for o, c, z in zip(original, changed, cost):
            transform_cost[(o, c)] = min(transform_cost[(o, c)], z)
        
        # Use Floyd-Warshall algorithm to compute minimum cost for all transformations
        all_chars = set(original) | set(changed)
        for k in all_chars:
            for i in all_chars:
                for j in all_chars:
                    if (i, k) in transform_cost and (k, j) in transform_cost:
                        transform_cost[(i, j)] = min(
                            transform_cost[(i, j)], 
                            transform_cost[(i, k)] + transform_cost[(k, j)]
                        )
        
        # Calculate the total cost to convert source to target
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            if (s, t) in transform_cost and transform_cost[(s, t)] != float('inf'):
                total_cost += transform_cost[(s, t)]
            else:
                return -1  # If transformation is impossible

        return total_cost
