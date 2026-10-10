class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dictionary = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            dictionary[sorted_word].append(word)
        return list(dictionary.values())