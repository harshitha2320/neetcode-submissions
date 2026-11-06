class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        res=0
        while l<r:
          min_h= min(heights[l],heights[r])
          min_w = r-l
          area = min_h*min_w
          if area>res:
            res=area
          if heights[l]>heights[r]:
            r-=1
          else:
            l+=1
        return res



        