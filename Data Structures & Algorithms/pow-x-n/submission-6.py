class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if n == 0:
                return 1
            
            res = pow(x, n // 2)
            res *= res
            return res * x if n % 2 else res
        
        return pow(x, n) if n >= 0 else 1 / pow(x, -n)
        