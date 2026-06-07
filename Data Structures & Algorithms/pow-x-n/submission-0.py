class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = pow(x, n // 2)
            
            if n % 2:
                return res * res * x
            else:
                return res * res
        
        return pow(x, n) if n > 0 else 1 / pow(x, -n)
