class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num]+=1
            else:
                hash_table[num] = 1
        
        for key, value in hash_table.items():
            if value > 1:
                return True
        return False
