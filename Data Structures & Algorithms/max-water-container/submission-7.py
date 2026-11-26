class Solution:
    def maxArea(self, h: List[int]) -> int:
        i,j=0,len(h)-1 
        res=0
        while i<j:
            area = min(h[i],h[j]) * (j-i)
            if res <area:
                res=area
            if h[i]>h[j]:
                j-=1
            else:
                i+=1
        return res
