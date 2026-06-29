class Solution:
    def isValid(self, s: str) -> bool:
        stck=[]
        opening="([{"
        closing=")]}"
        for i in s:
            if i in opening:
                stck.append(i)
            else:
                if(len(stck)==0):
                    return False
                if(opening.index(stck.pop())!=closing.index(i)):
                    return False
        if not stck:
            return True
        else:
            return False
        