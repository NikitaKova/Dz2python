a = int(input())
list_num = []
factorial = 1
for i in range(2, a+1):
    list_num.append(factorial)
    factorial*=i
print(list_num)