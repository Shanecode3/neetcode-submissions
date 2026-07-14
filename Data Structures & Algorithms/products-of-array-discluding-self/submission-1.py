class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        pref=suf=1
        
        for i in range(0,n):
            res[i]=pref
            pref*=nums[i]
        for i in range(n-1,-1,-1):
            res[i]*=suf
            suf*=nums[i]
        return res