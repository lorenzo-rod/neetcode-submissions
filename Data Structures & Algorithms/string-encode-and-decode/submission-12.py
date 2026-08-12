class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for string in strs:
            res.append("".join([str(len(string)), "#", string]))
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            count = 0
            while s[i] != "#":
                count = 10 * count + int(s[i])
                i += 1
            
            res.append(s[i+1:i+1+count])
            i += count + 1
        
        return res



