class Solution:
    def minMoves2(self, nums):
        nums.sort()
        median = nums[len(nums) // 2]  # Find the median
        return sum(abs(num - median) for num in nums)  # Sum of differences from median
