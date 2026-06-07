class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_length = 0

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                while(s[left] != s[right]):
                    seen.discard(s[left])
                    left += 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length