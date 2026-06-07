class Solution:

    def encode(self, strs: List[str]) -> str:
        code = []
        for s in strs:
            code.append("".join([str(len(s)), "#"]))
            code.append(s)
        return "".join(code)
    
    def decode(self, s: str) -> List[str]:
        index = 0
        res = []
        print(s)
        while(index < len(s)):
            count = 0
            while(s[index] != "#"):
                count = 10 * count + int(s[index])
                index += 1
            index += 1
            word = []
            for _ in range(count):
                word.append(s[index])
                index += 1
            res.append("".join(word))
        return res