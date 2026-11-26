class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx =0
        count =0
        for n in nums:
            if n != val:
                nums[idx] = n
                idx+=1
                count +=1
        return count

        