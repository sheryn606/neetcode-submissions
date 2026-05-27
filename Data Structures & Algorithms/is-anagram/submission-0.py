class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count,count1={},{}
        for sl in s:
            count[sl]=count.get(sl,0)+1
        for s2 in t:
            count1[s2]=count1.get(s2,0)+1
        if count==count1:
            return True
        else:
            return False
