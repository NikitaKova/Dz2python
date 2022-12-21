file = open("file.txt","r")
a = file.readlines()
print(a)
for i in range(len(a)):
    a[i] = int(a[i].strip())
print(a)
multy = 1
for i in range(len(a)):
    multy*=list_num[a[i]]
print(multy)
list_num = list(map(str.strip,a))
print(list_num)