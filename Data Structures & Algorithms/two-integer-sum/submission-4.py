class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash.keys() and hash[complement] != i:
                return [hash[complement],i]
            hash[nums[i]] = i