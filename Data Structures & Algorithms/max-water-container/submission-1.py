class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvolume=0
        i=0
        j=len(heights)-1
        while(i<j):
            maxvolume=max(maxvolume,(j-i)*min(heights[i],heights[j]))
            if(heights[i]<heights[j]):
                i=i+1
            else:
                j=j-1
        return maxvolume