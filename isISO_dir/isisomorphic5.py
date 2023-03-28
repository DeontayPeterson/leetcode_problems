
'9.1% ...'
def isIsomorphic(s:str, t:str) -> bool:
    pairs = {}

    for i in range(0, len(s)):
        
        if s[i] not in pairs.keys() and t[i] in pairs.values():
            return False

        elif s[i] not in pairs.keys():
            pairs[s[i]] = t[i]

        elif pairs[s[i]] != t[i]:
            return False

    return True

print(isIsomorphic('egg', 'add'))














