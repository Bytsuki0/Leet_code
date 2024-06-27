class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -1 * x
            str_num = str(x)
            str_num = str_num[::-1]
            str_num = "-" + str_num

        else:
            str_num = str(x)
            str_num = str_num[::-1]

        
        if int(str_num) > 2**31 - 1 or int(str_num) < -2**31:
            return 0
        else:
            return int(str_num)