class Solution:
    def isValid(self, s: str) -> bool:
        m = list(s) 
        test = []
        t = 0

        for i in range(0, len(m)):
            if m[i] == "(":
                test.append(1)
                t += 1
            elif m[i] == "[":
                test.append(2)
                t += 1
            elif m[i] == "{":
                test.append(3) 
                t += 1 
            elif m[i] == ")":
                if len(test) > 0 and test[t-1] == 1:
                    test.pop()
                    t -= 1
                else:
                    return False
            elif m[i] == "]":
                if len(test) > 0 and test[t-1] == 2:
                    test.pop()
                    t -= 1
                else:
                    return False
            elif m[i] == "}":
                if len(test) > 0 and test[t-1] == 3:
                    test.pop()
                    t -= 1
                else:
                    return False           
        if len(test) == 0:
            return True
        else: 
            return False