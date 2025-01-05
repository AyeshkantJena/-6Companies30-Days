class Solution:
    def findRepeatedDnaSequences(self, s):
      
        if len(s) < 10: #Time complexity - O(n)
            return []
        
        # Map nucleotides to numbers for efficient hashing
        nucleotide_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3} #Adenosine, Cytosine, Glucosamine, Thymine
        
        # Use bit manipulation for hash rolling
        # Each nucleotide takes 2 bits 
        # So 10 nucleotides = 20 bits
        window_size = 10
        bit_size = 2  # no. of bits per nucleotide
        all_bits = (1 << (window_size * bit_size)) - 1  # mask for 20 bits
        
        curr_hash = 0
        seen = set()
        repeated = set()
        
        # Calculate hash for first window
        for i in range(window_size):
            curr_hash = (curr_hash << bit_size) | nucleotide_map[s[i]]
            
        seen.add(curr_hash)
        
        # Use rolling hash for remaining windows
        for i in range(window_size, len(s)):
            # Remove leftmost nucleotide and add new nucleotide
            curr_hash = ((curr_hash << bit_size) & all_bits) | nucleotide_map[s[i]]
            
            if curr_hash in seen:
                repeated.add(s[i - window_size + 1:i + 1])
            else:
                seen.add(curr_hash)
                
        return list(repeated)