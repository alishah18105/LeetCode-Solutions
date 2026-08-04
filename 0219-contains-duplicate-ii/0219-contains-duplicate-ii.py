class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i in range(0, len(nums)):
            if nums[i] in hash_map:
                absolute = abs(hash_map[nums[i]] - i)
                if(absolute <= k):
                    return True
                else:
                    hash_map[nums[i]] = i
            else:
                hash_map[nums[i]] = i
        return False
