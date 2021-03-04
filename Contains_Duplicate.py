from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        a = Counter(nums)

        for i in range(0, len(nums)):
            if a[nums[i]] != 1:
                return True

        return False
