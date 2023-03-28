
from string import ascii_uppercase

case3 = 701 # -> ZY
test_case = 18226

def convertTitle(n: int) -> str:
    title = []
    letters = [l for l in ascii_uppercase]
    while n > 0:
        
        title.append(letters[(n-1)%26])
        n = (n-1) // 26

    title.reverse()
    answer = "".join(title)
    return answer

print(convertTitle(500))



