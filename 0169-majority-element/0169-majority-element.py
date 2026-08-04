class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(0, len(nums)):
            if(nums[i] in hash_map):
                hash_map[nums[i]] +=1
            else:
                hash_map[nums[i]] = 1
        
        max_value = len(nums) // 2
        major = 0
        
        for key, value in hash_map.items():
            if(value > max_value):
                major = key
        return major
