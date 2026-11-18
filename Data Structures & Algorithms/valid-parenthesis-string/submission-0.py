class Solution:
    def checkValidString(self, s: str) -> bool:
        stackleft=[]
        stackp=[]
        for i,c in enumerate(s):
            if c=="(":
                stackleft.append((c,i))
            if c=="*":
                stackp.append((c,i))
            if c==")":
                if stackleft:
                    stackleft.pop()
                else:
                    if stackp:
                        stackp.pop()
                    else:
                        return False
        while stackleft:
            if not stackp:
                return False
            left,idx=stackleft.pop()
            p,idxp=stackp.pop()
            if idx>=idxp:
                return False
        return True
                