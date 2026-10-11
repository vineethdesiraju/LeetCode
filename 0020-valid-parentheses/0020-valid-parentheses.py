class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(','}':'{', ']':'[' }
        stack=[]
        for c in s:
            if c not in d:  #basically if c is an opening bracekt,,,because d has keys of only closing brackets
                stack.append(c)
            else:
                if len(stack)==0: #if stack is empty and we came across a closing bracket
                    return  False
                else:
                    popp=stack.pop()
                    if popp!=d[c]:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
            


