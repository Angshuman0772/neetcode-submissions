class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict # handles case when key doesn't exist 
        anagram_groups = defaultdict(list)

        for word in strs: # sorting each word in the list
            sorted_word = tuple(sorted(word)) # key
            anagram_groups[sorted_word].append(word)
        return list(anagram_groups.values())

''' class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            anagram_groups = {}  # regular dictionary
            
            for word in strs:
                key = tuple(sorted(word))  # use sorted tuple as key
                
                if key not in anagram_groups:
                    anagram_groups[key] = []  # initialize list if key doesn't exist
                
                anagram_groups[key].append(word)  # add word to the group
            
            return list(anagram_groups.values()) '''
