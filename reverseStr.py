class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack1 = []
        if len(s)==1 :
            stack1.append(s)
        for idx in range(len(s)) :
            if s[idx] != "(" and not stack1 :
                stack1.append(s[idx])
                
            elif s[idx] == "(" and s[idx-1] == "(":
                stack1.append("")    
                
            elif (s[idx] != "(" and s[idx] != ")" ):
                if s[idx -1 ] == "(" :
                    stack1.append(s[idx])
                elif (s[idx -1 ] != "(" ) or (s[idx -1 ] == ")" ):
                    if stack1:
                        stack1[-1] = stack1[-1] + s[idx]
                    else:
                        stack1.append(s[idx])
                                
                    
            elif stack1 and s[idx] == ")" and s[idx-1] != "(" :
                x = (stack1.pop())[::-1]
                if stack1:
                    stack1[-1] = stack1[-1] + x
                else:
                    stack1.append(x)
            
                    
        return stack1.pop()
