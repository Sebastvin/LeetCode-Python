class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = len(digits) - 1
        zeros = 0

        while digits[tmp] > 8:
            if tmp == 0:
                break
            tmp -= 1
            zeros += 1

        digits[tmp] += 1
        tmp += 1

        if zeros > 0:
            for i in range(tmp, tmp + zeros):
                digits[i] = 0
                
        if digits[0] >= 10:
            digits.insert(1, digits[0] % 10)
            digits[0] //= 10
                
        return digits
