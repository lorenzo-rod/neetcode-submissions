class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append("".join([str(len(s)), "#"]))
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            len_s = 0

            while s[i] != '#':
                len_s = int(s[i]) + len_s * 10
                i += 1

            i += 1

            res.append(s[i:i+len_s])

            i += len_s
        
        return res
