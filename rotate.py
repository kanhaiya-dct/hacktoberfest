class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # handle k > n
        
        # Reverse entire array
        self.reverse(nums, 0, n - 1)
        # Reverse first k elements
        self.reverse(nums, 0, k - 1)
        # Reverse remaining elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: list[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
