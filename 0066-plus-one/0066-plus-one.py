class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = digits[-1] + 1
        carry = number // 10
        digits[-1] = number % 10
        for i in range(len(digits) - 2, -1, -1):
            if carry == 0:
                break
            number = digits[i] + carry
            carry = number // 10
            digits[i] = number % 10
        if carry > 0:
            digits.insert(0, carry)
        return digits