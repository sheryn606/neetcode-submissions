class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left={}
        result=[]
        right={}
        product=1
        left[0]=1
        prodr=1
        right[len(nums)-1]=1
        for i in range(1,len(nums)):
            left[i]=product*nums[i-1]
            product=product*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i]=prodr*nums[i+1] 
            prodr=prodr*nums[i+1]
        for i in range(len(nums)):
            result.append(left[i]*right[i])
        return result
            