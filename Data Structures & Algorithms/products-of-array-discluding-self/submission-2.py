class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        pref=suf=1
        
        for i,n in enumerate(nums):
            res[i]=pref
            pref*=nums[i]
        for i,n in reversed(list(enumerate(nums))):
            res[i]*=suf
            suf*=nums[i]
        return res