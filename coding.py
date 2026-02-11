class Solution:
    def twoSum(self,nums:List[int],target:int) -> List[int]:
        val_ind = {}
        for i,num in enumerate(nums):
            if target-num in val_ind:
                return[val_ind[target-num],i]
            val_ind[num] = i
            