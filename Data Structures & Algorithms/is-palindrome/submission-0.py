class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = "".join(ch.lower() for ch in s if ch.isalnum())
        l,r=0,len(str1)-1
        while l<r:
            if str1[l]==str1[r]:
                l+=1
                r-=1
            else:
                return False   
        return True
