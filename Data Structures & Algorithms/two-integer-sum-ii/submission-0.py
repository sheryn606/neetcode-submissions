class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result={}
        pos=0
        j=0
        for i in range(len(numbers)):
            pos=result.get(numbers[i],-1)
            if(pos==-1):
                result[target-numbers[i]]=i
            else:
                print(sorted([i+1,pos+1]))
                j=i
                break
                
                
        return sorted([j+1,pos+1])
        
        