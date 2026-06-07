class Solution:

    def encode(self, strs: List[str]) -> str:
        code = []
        for string in strs:
            code.append(str(len(string)))
            code.append("#")
            code.append(string)
        return "".join(code)

    def decode(self, s: str) -> List[str]:
        index = 0
        count = 0
        res = []
        word = []
        while (index < len(s)):
            while (s[index] != "#"):
                count = count * 10 + int(s[index])
                index += 1
            index += 1
            word = []
            for i in range(count):
                word.append(s[index + i])
            index += count
            res.append("".join(word))
            count = 0
        return res