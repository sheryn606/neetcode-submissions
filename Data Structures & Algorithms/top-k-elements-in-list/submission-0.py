class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        list1=[]
        for i in range(len(nums)):
            dict1[nums[i]]=dict1.get(nums[i],0)+1
        sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
        for i in range(k):
            list1.append(list(sorted_dict.keys())[i])
        return list1