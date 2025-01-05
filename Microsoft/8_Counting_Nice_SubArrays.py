class Solution:
    def numberOfSubarrays(self, nums, k):
        """
        Count subarrays with exactly k odd numbers using prefix sum approach.
        Args:
            nums: List of integers
            k: Target count of odd numbers
        Returns:
            Number of valid subarrays
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        # Store count of subarrays ending at current position
        count = 0
        # Store current count of odd numbers
        curr_odd = 0
        # Store the first index of each count of odd numbers
        odd_count_indices = [0] * (n + 1)
        odd_count_indices[0] = 1  # Empty subarray has 0 odd numbers
        
        for num in nums:
            # Update current count of odd numbers
            curr_odd += num & 1  # Faster than num % 2
            
            # If we have at least k odd numbers, add count of previous valid windows
            if curr_odd >= k:
                count += odd_count_indices[curr_odd - k]
                
            # Update count of windows with current odd count
            odd_count_indices[curr_odd] += 1
            
        return count

        