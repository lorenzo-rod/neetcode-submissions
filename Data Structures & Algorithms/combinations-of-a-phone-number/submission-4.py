class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        n = len(digits)

        digits_map = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        combinations = []

        def backtrack(combination, i):
            if len(combination) == n:
                combinations.append("".join(combination))
                return
            
            for c in digits_map[digits[i]]:
                combination.append(c)
                backtrack(combination, i+1)
                combination.pop()
        
        backtrack([], 0)
        return combinations
