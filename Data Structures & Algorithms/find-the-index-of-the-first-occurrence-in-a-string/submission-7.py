class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                if i + len(needle) <= len(haystack) and haystack[i:i+len(needle)] == needle:
                    return i           
            i += 1       
        return -1