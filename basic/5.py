vowel = "aeiou"
a = "aaii"
list1 = {}
for i in vowel:
    b = a.count(i)
    c = {i:b}
    list1.update(c)
e = list(list1.values())
d= max(e)
print(d)
# list2=[]
# for j in list1.get(d):  
#     list2.append(j)