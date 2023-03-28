p1 = "abba"
s1 = "dog cat cat dog"


# def wordPattern(pattern: str, s: str) -> bool:
#     pairs = {}
#     words = s.split()
#     if len(words) != len(pattern):
#         return False
    
#     for i in range(len(pattern)):
#         if pattern[i] in pairs.keys():
#             if pairs[pattern[i]] == words[i]:
#                 continue
#             else:
#                 return False
#         else:
#             if words[i] in pairs.values():
#                 return False
#             else:
#                 pairs[pattern[i]] = words[i]
#     return True

p1 = set(p1)
s1 = set(s1.split())

x = zip(p1, s1)

print(list(x))