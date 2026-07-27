class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxarea=0
        while l<r:
            minheight=min(heights[l],heights[r])
            area=minheight*(r-l)
            if heights[l] == minheight:
                l+=1
            elif heights[r] == minheight:
                r-=1
            maxarea=max(area,maxarea)
        return maxarea
                