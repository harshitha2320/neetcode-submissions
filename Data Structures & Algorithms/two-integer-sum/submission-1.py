class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)+1):
            comp = target - nums[i]
            if comp in dict:
                return [dict[comp],i]
            dict[nums[i]]=i
        return []
