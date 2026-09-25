class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """"
        Generemos un mapa hash para poder realizar un guardado  
        """
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash.keys() and hash[complement] != i:
                return [hash[complement],i] # el primero es el guardado en el hash entonces lo sabemos de antemano , i es el indice del complemento con certeza.
            hash[nums[i]] = i