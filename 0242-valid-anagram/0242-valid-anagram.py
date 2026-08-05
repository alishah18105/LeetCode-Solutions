class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq1 = {}
        if(len(s) != len(t)):
            return False
        else:
            for i in range(len(s)):
                if s[i] in char_freq1:
                    char_freq1[s[i]] +=1
                else:
                    char_freq1[s[i]] = 1
            
            char_freq2 = {}
            for i in range(len(t)):
                if t[i] in char_freq2:
                    char_freq2[t[i]] +=1
                
                else:
                    char_freq2[t[i]] = 1
        
            if (char_freq1 == char_freq2):
                return True
            
            else:
                return False
