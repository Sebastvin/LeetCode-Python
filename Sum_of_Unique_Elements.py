class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = Counter(nums)
        result = []

        for i in range(0, len(nums)):
            if a[nums[i]] == 1:
                result.append(nums[i])
                

        return sum(result)
