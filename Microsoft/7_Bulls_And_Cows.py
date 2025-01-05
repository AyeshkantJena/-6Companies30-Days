from collections import Counter

class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        secret_counts = Counter()
        guess_counts = Counter()

        # First pass: count bulls and keep track of remaining unmatched digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counts[s] += 1
                guess_counts[g] += 1

        # Second pass: count cows using the minimum overlap between unmatched digits
        cows = sum(min(secret_counts[d], guess_counts[d]) for d in secret_counts)

        return str(bulls) + "A" + str(cows) + "B"
