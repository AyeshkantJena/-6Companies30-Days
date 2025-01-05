class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)
        mid = (n - 1) // 2  # Middle index for the smaller half

        # Create a copy of nums split into two halves and reversed
        small_half = nums[:mid + 1][::-1]
        large_half = nums[mid + 1:][::-1]

        # Fill nums with alternating elements from small_half and large_half
        nums[::2] = small_half
        nums[1::2] = large_half