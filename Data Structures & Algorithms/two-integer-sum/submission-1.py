class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # string is key, value is index
        numL = {}
        for i,n in enumerate(nums):
            diff = target-n # diff is number looked for  
            if diff in numL: # if diff is in the hashmap we return it
                return [numL[diff],i];
            numL[n] = i # we keep going 
            