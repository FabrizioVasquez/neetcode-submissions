class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hasmap.keys():
                return [hasmap[diff],i]
            else:
                hasmap[nums[i]] = i