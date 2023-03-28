
#Terrible 5.1%
def isIsomorphic(s: str, t: str) -> bool:
    enc = set()

    for i in range(0, len(s)):

        v1 = s[i]
        v2 = t[i]

        if v1 not in enc:

            i1 = [i for i,v in enumerate(s) if v == v1]
            i2 = [i for i,v in enumerate(t) if v == v2]

            if i1 != i2:
                return False
        enc.add(v1)
    return True


isIsomorphic('leet', 'code')