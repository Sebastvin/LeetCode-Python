class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        counter = 0
        x = '{:032b}'.format(x)
        y = '{:032b}'.format(y)
        
        for i in range(0, len(x)):
            if x[i] != y[i]:
                counter += 1
        
        return counter
