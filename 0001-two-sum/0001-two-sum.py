class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}  # Dictionary to store number and its index
        for i in range(len(nums)):
            value=nums[i]
            difference=target-value
            if value not in d:
                d[difference]=i
            else:
                current_index=i
                prev_index=d[value]
                return [current_index, prev_index]