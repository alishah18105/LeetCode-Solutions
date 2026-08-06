class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward_map = {}
        reverse_map = {}
        
        for i in range(len(s)):
            if s[i] in forward_map:
                if forward_map[s[i]] != t[i]:
                    return False
            else:
                forward_map[s[i]] = t[i]

            if t[i] in reverse_map:
                if reverse_map[t[i]] != s[i]:
                    return False
            else:
                reverse_map[t[i]] = s[i]

        return True

