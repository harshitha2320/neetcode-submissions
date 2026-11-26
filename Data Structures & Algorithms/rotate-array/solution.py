class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=0
        r = k%len(nums)
        while idx<r:
            nums.insert(0,nums[-1])
            nums.pop()
            idx+=1
