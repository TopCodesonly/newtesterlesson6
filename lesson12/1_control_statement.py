for i in range(10):
    if i == 4:
        break
    print(i)#0123

n=0
while n<10:
    if n==5:
        break
    print(n)
    n+=1

#Continue

for i in range(10):
    if i == 5:
        continue
    print(i) # 0,1,2,3,4,5,6,7,8,9

n=9
while n < 10:
    if n == 5:
        continue
    print(n)
    n+=1

