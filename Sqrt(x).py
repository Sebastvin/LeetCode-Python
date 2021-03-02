import math  
class Solution:
    def mySqrt(self, x: int) -> int:
        
        num = str(math.sqrt(x))
        result = ""

        for i in range(0, len(num)):
            if num[i] != '.':
                result+=num[i]
            else:
                break
        
        return int(result)
