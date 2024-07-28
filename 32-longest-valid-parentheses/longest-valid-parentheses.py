class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pilha = [-1]
        lenght = 0

        for i in range(len(s)):
            if s[i] == "(":
                pilha.append(i)
            else:
                pilha.pop()
                if len(pilha) == 0:
                    pilha.append(i)
                else:
                    lenght = max(lenght, i - pilha[-1])
        
        return lenght