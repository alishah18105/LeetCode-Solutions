class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = set()
        for num in nums:
            if num in hash_table:
                return True
            else:
                hash_table.add(num)
        return False
