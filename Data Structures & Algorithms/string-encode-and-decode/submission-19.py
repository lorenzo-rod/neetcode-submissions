class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        i = 0
        n = len(s)
        res = []

        while i < n:

            length = 0

            while s[i] != "#":
                length *= 10
                length += int(s[i])
                i += 1

            i += 1
            res.append(s[i:i+length])
            i += length
        
        return res
        

