class Solution:
    def reverseWords(self, s: str) -> str:
        
        result = ""
        s = s.split()
        
        for i in range(0, len(s)):
            if len(s) -1 != i:
                result += s[i][::-1] + " "
            else:
                result += s[i][::-1]
            
        return result
