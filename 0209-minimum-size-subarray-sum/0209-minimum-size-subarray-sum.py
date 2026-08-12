class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        min_length = float('inf')
        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                current_length  = right - left + 1
                min_length = min(min_length, current_length)
                window_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0
        else:
            return min_length
        