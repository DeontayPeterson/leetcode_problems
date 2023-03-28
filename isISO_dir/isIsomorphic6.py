

def isIsomorphic(s: str, t: str) -> bool:
    pairs = {}
    enc = set()

    for i in range(0, len(s)):
        
        if s[i] in pairs:
            if pairs[s[i]] != t[i]:
                return False
        elif t[i] in enc:
            return False
        elif s[i] not in pairs:
            pairs[s[i]] = t[i]
            enc.add(t[i])
    return True


print(isIsomorphic('egcd', 'adfd'))
print(isIsomorphic('egg', 'add'))
isIsomorphic('leet', 'code')
