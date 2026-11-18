class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket={'(':')',"{":"}","[":"]"}
        for i in s:
            if i in bracket:
                stack.append(i)
            else:
                if stack and bracket[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True