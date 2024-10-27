def reverse_list(lst):
    lst.reverse()


lst = [1,2,6,7,9]
reverse_list(lst)
print(lst)

# on peut comparer deux listes et dire si elles sont pareil ou pas 
a = [1,2,3]
b = [1,2,3] #true

c = [1,2,3]
d = [1,2,3,4] # false
if a == b:
    print("true")
else:
    print("false")