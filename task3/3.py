a = int(input())
dict_num = {}
for i in range(1, a+1):
    dict_num[i] = round((1+1/i)**i,2)
print(dict_num)