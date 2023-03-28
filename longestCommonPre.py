
case1 = ["flower","flow","flight"]
case2 = ["dog","racecar","car"]
case3 = ['ab', 'a']

# def longestCommonPrefix(strs):
#     if "" in strs:
#         return ""
#     if len(strs) == 1:
#         return strs[0]

#     shortest = len(min((word for word in strs if word), key=len))
#     i = 0
#     prefix = ""
#     enc = set()

#     while i <= shortest-1:
#         for w in range(0, len(strs)):
#             enc.add(strs[w][i])

#         if len(enc) == 1:
#             prefix += enc.pop()
#             enc.clear()
#             i += 1
#         else:
#             break

#     return prefix
        
# print(longestCommonPrefix(case3))



def LongestCommonPrefix(strs):
    prefix = ""
    for i in range(0,len(strs[0])):
        current = strs[0][i]
        for word in strs:
            if len(word) == i or word[i] != current:
                return prefix
        prefix += current
    return prefix