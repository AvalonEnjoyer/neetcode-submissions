class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 !=0:
            return False
        stack=[]
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                match s[i]:
                    case ')':
                        if stack.pop() == '(':
                            continue
                        else:
                            return False
                    case ']':
                        if stack.pop() == '[':
                            continue
                        else:
                            return False
                    case '}':
                        if stack.pop() == '{':
                            continue
                        else:
                            return False
        if len(stack)!=0:
            return False
        return True