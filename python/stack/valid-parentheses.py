class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closedToOpenMap = {")":"(", "}":"{", "]": "["}
        
        for x in s:
            if x in closedToOpenMap:
                if stack and stack[-1] == closedToOpenMap[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        
        return not stack
