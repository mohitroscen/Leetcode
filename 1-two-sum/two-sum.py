class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}  # Dictionary to store number and its index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            d[nums[i]] = i
        return []  
