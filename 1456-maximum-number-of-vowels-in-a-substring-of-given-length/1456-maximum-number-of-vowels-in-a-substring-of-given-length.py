class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a","e", "i", "o", "u"]
        count = 0
        max_count = 0
        for i in range(0,k):
            if s[i] in vowels:
                count+=1
        max_count = count

        for right in range(k, len(s)):
            left = right - k
            if s[left] in vowels:
                count-=1
            if s[right] in vowels:
                count+=1
            max_count = max(count,max_count)
            
        return max_count