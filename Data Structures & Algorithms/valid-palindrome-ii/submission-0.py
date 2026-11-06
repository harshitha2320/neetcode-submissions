class Solution:
    def validPalindrome(self, s: str) -> bool:
        char = ''.join(c.lower() for c in s if c.isalnum())

        l,r=0,len(char)-1
        while l<r:
            if char[l]!=char[r]:
                skipL,skipR = char[l+1:r+1], char[l:r]
                return(skipL==skipL[::-1] or skipR==skipR[::-1])
            else:
                l+=1
                r-=1
        return True        