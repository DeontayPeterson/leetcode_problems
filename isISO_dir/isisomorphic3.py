
#Exceeds time limit
def isIsomorphic(s: str, t: str) -> bool:

    for i in range(0, len(s)):
        v1 = s[i]
        v2 = t[i]

        i1 = [i for i,v in enumerate(s) if v == v1]
        i2 = [i for i,v in enumerate(t) if v == v2]
        print(i1, "/", i2)

        if i1 != i2:
            return False
    return True


