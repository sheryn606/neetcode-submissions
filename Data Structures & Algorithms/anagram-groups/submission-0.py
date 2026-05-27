class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        from collections import defaultdict
        table = defaultdict(list)
        for i in range(len(strs)):
            sorts=''.join(sorted(strs[i]))
            table[sorts].append(i)
        result=[[strs[x] for x in y] for y in table.values()]
        return result
           
