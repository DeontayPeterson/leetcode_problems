
'''
egcd
adfd
'''

'''
"abab"-> "baba"
egg->add

'''

## 43/44 CASES.

def isIsomorphic(s: str, t: str) -> bool:

    enc = set()
    temp = list(s)

    for i,v in enumerate(t):
        if v in enc:
            pass
        else:
            to_replace = s[i]
            locs = [index for index, value in enumerate(s) if value == to_replace]
            for i in locs:
                temp[i] = v
            print(temp)
        enc.add(v)
        enc.add(s[i])

    if "".join(temp) == t:
        return True
    return False
    
print(isIsomorphic('egcd', 'adfd'))

    
