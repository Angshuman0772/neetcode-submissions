class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0

        "5#Hello5#World"
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l: r])
            result.append(s[r + 1 : r + length + 1])
            l = length + 1 + r
    
        return result