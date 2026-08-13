class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        max_length = 0
        left = 0

        for right in range(len(s)):

            while s[right] in hash_set:
                hash_set.discard(s[left])
                left += 1

            hash_set.add(s[right])

            current_length = right - left + 1
            max_length = max(current_length, max_length)

        return max_length

            