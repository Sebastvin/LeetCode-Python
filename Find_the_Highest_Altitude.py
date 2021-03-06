class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        result = [0]

        for i in range(0, len(gain)):
            result.append(gain[i] + result[i])
            
        return max(result)
