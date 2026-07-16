class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.replace(" ","").lower()
        s2="".join(c for c in s1 if c.isalnum())
        l=0
        r=len(s2)-1
        while l<r:
            if s2[l]==s2[r]:
                l+=1
                r-=1
            else:
                return False
        return True
            
