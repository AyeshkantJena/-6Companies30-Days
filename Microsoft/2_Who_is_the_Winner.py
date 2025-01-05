class Solution:
    def findTheWinner(self, n, k):
        friends = list(range(1, n + 1))
        idx = 0  # Start at the first friend
        
        # Eliminate friends until only one is left
        while len(friends) > 1:
            # Indexing of the friend to remove
            idx = (idx + k - 1) % len(friends)
            # Removal of the friend after calculation
            friends.pop(idx)
        
        # Return the last remaining friend
        return friends[0]