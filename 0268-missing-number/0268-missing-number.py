class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        for i in range(0, len(nums)+1):
            sum1+= i
        sum2 = 0
        for i in range(0,len(nums)):
            sum2 += nums[i]
        
        return sum1-sum2

        