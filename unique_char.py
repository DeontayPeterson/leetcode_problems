
class Solution:
    def firstUniqChar_SLOW(self, s: str) -> int:
        '''
        At most you have to iterate over the string 26 times, but for very long strings
        this takes a long time.
        '''
        enc = set()
        for i, char in enumerate(s):
            if not char in enc:
                if s.count(char) == 1:
                    return i 
        return -1


def firstUniqChar(s: str) -> int:
    '''
    20x faster
    '''
    enc = {}
    for char in s:
        if char in enc:
            enc[char] +=1 
        else:
            enc[char] = 1

    for i, char in enumerate(s):
        if enc[char] == 1:
            return i 
    return -1
        




s = 'leetcode'
x = s.find('e')
print(x)
y = s.rfind('e')
print(y)



