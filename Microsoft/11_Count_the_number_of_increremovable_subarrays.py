class Solution:
    def incremovableSubarrayCount(self, nums):
        n = len(nums)
        result = 0
        
        for start in range(n):
            for end in range(start, n):
                subarray = nums[start:end+1]
                remaining = nums[:start] + nums[end+1:]
                if self.is_strictly_increasing(remaining):
                    result += 1

        return result