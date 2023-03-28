
def findTheDifference(s: str, t: str) -> str:

    #First Try..

    s_dict = {}
    t_dict = {}

    for char in s:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1
    for char in t:
        if char in t_dict:
            t_dict[char] += 1
        else:
            t_dict[char] =1

    for key in t_dict.keys():
        if key not in s_dict:
            return key
        elif s_dict[key] != t_dict[key]:
            return key
        

def findTheDifference2(s: str, t: str) -> str:

    s1, t1 = 0, 0

    for c in s:
        s1 += ord(c)

    for c in t:
        t1 += ord(c)

    return chr(t1-s1)


print(findTheDifference2('abc', 'abcd'))