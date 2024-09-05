class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        combinations = []
        self.backtrack(0, [], digits, digit_mapping, combinations)
        return combinations

    def backtrack(self, index: int, path: List[str], digits: str, letters: dict, combinations: List[str]):
        if len(path) == len(digits):
            combinations.append(''.join(path))
            return
        
        possible_letters = letters[digits[index]]
        
        for letter in possible_letters:
            path.append(letter)
            self.backtrack(index + 1, path, digits, letters, combinations)
            path.pop()