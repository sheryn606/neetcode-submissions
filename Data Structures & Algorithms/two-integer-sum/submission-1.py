class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={nums[0]:0}
        for i in range(1,len(nums)):
            diff=target-nums[i]
            if(diff in dict1):
                return [dict1[diff],i]
            dict1[nums[i]]=i
        
       

            