class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
            can = True
            nums = []
            result = []
            
        
            for i in range(left, right +1):
                nums = list(map(int, str(i)))
                if 0 in nums:
                    continue

                for j in range(0, len(nums)):
                    if i % nums[j] != 0:
                        can = False

                if can:
                    result.append(i)
                can = True


            return result
