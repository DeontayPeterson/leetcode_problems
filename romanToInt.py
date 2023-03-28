# def romanToInt(s: str) -> int:
#     total = 0
#     roman = {
#     "I":1,
#     "V":5,
#     "X":10,
#     "L":50,
#     "C":100,
#     "D":500,
#     "M":1000,
#     }
#     romans = {    
#     'IV': 4,
#     'IX': 9,
#     'XL': 40,
#     'XC': 90,
#     'CD': 400,
#     'CM': 900
#     }

#     twos = [s[i:i+2] for i in range(0,len(s)-1)]
#     for i in twos:
#         if i in romans:
#             total += romans[i]
#             s = s.replace(i, '_')
#     for char in s:
#         if char in roman:
#             total += roman[char]
#     return total


# print(romanToInt('MCMXCIV'))

def romanToInt(s:str) -> int:
    t1 = 0
    prev = 0 
    roman = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
    }


    for c in s:
        if roman[c] > prev:
            t1 += roman[c]
        else:
            t1 -= roman[c]
        prev = roman[c]
    print(t1)


romanToInt('MCMXCIV')