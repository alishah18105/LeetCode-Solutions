class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {}
        window_sum = 0
        max_sum = 0
        
        for i in range(k):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1
            window_sum+= nums[i]
            if len(hash_map) == k:
                max_sum =  max(max_sum,window_sum)
        
        for right in range(k,len(nums)):
            left = right -k
            hash_map[nums[left]] -= 1
            window_sum -= nums[left]

            if hash_map[nums[left]] == 0:
                del hash_map[nums[left]]

            hash_map[nums[right]] = hash_map.get(nums[right],0)+1
            window_sum+= nums[right]
            if len(hash_map) == k:
                max_sum =  max(max_sum,window_sum)
        return max_sum
