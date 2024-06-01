class Solution:
    def scoreOfString(self, s: str) -> int:
        list = [ord(char) for char in s]
        sum = 0
        for i in range(len(list)- 1):
            sum = abs(list[i] - list[i + 1]) + sum
        return sum