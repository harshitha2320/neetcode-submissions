class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            count = [0]*26
            for s in word:
                count[ord(s) - ord('a')] += 1
            hashmap[tuple(count)].append(word)
        return list(hashmap.values())
        