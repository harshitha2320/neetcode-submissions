class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        top_k_elements = counts.most_common(k)
        result = [element for element, frequency in top_k_elements]
        return result 
