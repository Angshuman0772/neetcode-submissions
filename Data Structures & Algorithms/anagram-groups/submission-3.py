class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # sorted -> words

        for word in strs:
            sortedWord = tuple(sorted(word))
            hashMap[sortedWord].append(word)
        
        return list(hashMap.values())