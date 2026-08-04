class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while(True):
            sum = 0
            while(n != 0):
                last_digit = n % 10
                sum  = sum + (last_digit ** 2)
                n = n // 10
            if(sum == 1):
                return True
            else:
                if(sum in s):
                    return False
                else:
                    s.add(sum)
                    n = sum
                
                

