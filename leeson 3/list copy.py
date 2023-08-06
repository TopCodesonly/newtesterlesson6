#shallow copy

a=[[1,2,3],4,5]
b=a.copy()

a[0][1]=7
print(a)#[[1, 7, 3], 4, 5]
print(b)#[[1, 7, 3], 4, 5]



# deepcopy

from copy import deepcopy


a=[[1,2,3],4,5]
b=deepcopy(a)
a[0][1]=7

print(a)#[[1, 7, 3], 4, 5]
print(b)#[[1, 2, 3], 4, 5]