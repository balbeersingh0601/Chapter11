list=[]
for i in range(50):
    list+=[i]
print(list)
print(" Square of 1 to 50 ")
print()
list2=[]
for j in range(51):
    sqr=j*j
    list2+=[sqr]
print(list2)
print()
print("Sequence of alphabets ")
list3=[]
a=96
for k in range(27):
    term=chr(a)*k
    list3+=term
    a+=1
print(list3)
