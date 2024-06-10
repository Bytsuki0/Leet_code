import math
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while True:
            if i * i == x:
                return i 
                break
            elif (i * i) < x:
                i+= 1
            elif (i * i) > x:
                i-= 1
                return i
                break