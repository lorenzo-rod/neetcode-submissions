class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in reversed(range(n - 1)):
            j = i + 1

            while j < n:

                if temperatures[i] < temperatures[j]:
                    res[i] = j - i
                    break
                elif res[j] == 0:
                    break
                
                j += res[j]
                
        
        return res
                
