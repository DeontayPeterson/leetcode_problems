def isvalid(s:str):
    p = {
    '(':')',
    '{':'}',
    '[':']',
    }  
    stack = []

    for char in s:
        if char in p:
            stack.append(p[char])
        elif char in p.values() and stack[-1] == p[char]:
            stack.pop(-1)
        else:
            return False
            
