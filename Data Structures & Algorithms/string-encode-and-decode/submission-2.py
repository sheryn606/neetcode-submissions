class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        result=""
        for s in strs:
            result=result+chr(97+len(s))
            result = result+" ".join(letter for letter in s)
            encoded+=result
            result=""
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded=[]
        count=0
        result=""
        n=len(s)
        i=0
        while(i<len(s)):
            if(i%2==0):
                if(s[i]!=" "):
                    count=int(ord(s[i])-97)
                    if(s[i]=="a"):
                        s=s[:i+1]+" "+s[i+1:]
                        
            else:
                if count==0:
                    decoded.append("")
                    i+=1
                    continue
                result=result+s[i]
                count-=1
                if(count==0):
                    decoded.append(result)
                    result=""
            
            i+=1
            
        return decoded