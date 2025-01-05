class Solution:
    def maxProduct(self, s):
        n = len(s)
        max_product = 0

        # Precompute all palindromic subsequences using bitmasking
        is_palindrome = {}
        for mask in range(1 << n):
            subseq = ''.join(s[i] for i in range(n) if mask & (1 << i))
            is_palindrome[mask] = subseq == subseq[::-1]

        # Iterate over all subsets
        for mask1 in range(1 << n):
            if not is_palindrome[mask1]:
                continue
            len1 = bin(mask1).count('1')  # Count bits in mask1 (length of subsequence 1)
            
            # Mask2 is the complement of mask1 (remaining characters)
            mask2 = ((1 << n) - 1) ^ mask1
            submask = mask2
            while submask:
                if is_palindrome[submask]:
                    len2 = bin(submask).count('1')  # Count bits in mask2 (length of subsequence 2)
                    max_product = max(max_product, len1 * len2)
                submask = (submask - 1) & mask2  # Iterate over all submasks of mask2

        return max_product
