class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = defaultdict(list)
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            key[sorted_word].append(word)
        return list(key.values())