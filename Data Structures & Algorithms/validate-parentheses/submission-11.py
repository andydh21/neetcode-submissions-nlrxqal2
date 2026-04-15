class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        solution = []
        LP, LB, LC = 0, 0, 0 
        RP, RB, RC = 0, 0, 0

        # s = "[(])"
        for i in range(len(s)):
            if s[i] == "(":
                if RP > LP:
                    return False
                else:
                    solution.append(s[i])
                    LP += 1
            elif s[i] == ")":
                if s[i-1] != "[" and s[i-1] != "{":
                    if RP > LP:
                        return False
                    else:
                        solution.append(s[i])
                        RP += 1
                else:
                    return False
            
            elif s[i] == "[":
                if RB > LB:
                    return False
                else:
                    solution.append(s[i])
                    LB += 1
            elif s[i] == "]":
                if s[i-1] != "(" and s[i-1] != "{":
                    if RB > LB:
                        return False
                    else:
                        solution.append(s[i])
                        RB += 1
                else:
                    return False


            elif s[i] == "{":
                if RC > LC:
                    return False
                else: 
                    solution.append(s[i])
                    LC += 1
            elif s[i] == "}":
                if s[i-1] != "[" and s[i-1] != "(":
                    if RC > LC:
                        return False
                    else:
                        solution.append(s[i])
                        RC += 1
                else:
                    return False
        
        if LP != RP:
            return False
        elif LC != RC:
            return False
        elif LB != RB:
            return False
        else:
            return True    

             