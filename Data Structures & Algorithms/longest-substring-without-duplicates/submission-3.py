class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        maxlen = 0

        for r in range(len(s)):

            while s[r] in chars:
                # remove left character
                chars.remove(s[l])
                # move l
                l+=1
            # add current character
            chars.add(s[r])
            # update maxlen
            maxlen=max(maxlen,r-l+1)
        return maxlen