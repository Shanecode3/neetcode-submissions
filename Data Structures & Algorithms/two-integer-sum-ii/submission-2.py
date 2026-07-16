class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            csum=numbers[l]+numbers[r]
            if target>csum:
                l+=1
            elif target<csum:
                r-=1
            else:
                return[l+1, r+1]
        return[]