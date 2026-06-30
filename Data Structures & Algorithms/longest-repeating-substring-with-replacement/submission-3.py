class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        log={}
        l=0
        r=0
        maxWin=0
        while(r<len(s)):
            log[s[r]]=log.get(s[r],0)+1
            maxFreq=max(log.values())
            ch=r-l+1-maxFreq
            
            if(ch<=k):
                maxWin=max(r-l+1,maxWin)
                r+=1
            else:
                log[s[l]]=log[s[l]]-1
                l+=1
                r+=1
                
        return maxWin