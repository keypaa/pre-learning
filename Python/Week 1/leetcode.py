list1 = [1,2,4]
list2 = [1,3,4]


# solution = []

# for i in list1:
#     solution.append(i)
# for j in list2:
#     solution.append(j)

# print(solution)

# solution.sort()
# print(solution)
s = "{[]}"
class Solution:
    def isValid(self, s: str) -> bool:
        def has_matchings(s):
            return "{" in s and "}" in s and "[" in s and "]" in s and "(" in s and ")" in s
        
