#q7
my_list=['p','r','o','b','l','e','m']
my_list[2:3]=[]
print(my_list)
my_list[2:5]=[]
print(my_list)

#q8
List1=[13,18,11,16,13,18,13]
print(List1.index(18))
print(List1.count(18))
List1.append(List1.count(13))
print(List1)