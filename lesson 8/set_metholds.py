

m1={1,2,3,4,5,6}
m2=m1.copy()
print(m1)
print(m2)

# difference()
m1={1,2,3,4,5,6}
m2=[5,6,7,8]
diff= m1.difference(m2)
print(diff)#{1, 2, 3, 4, 5}
#diff=m1-m2 # we can also use - operator 
#print(diff)

# union()
m1={1,2,3,4,5,6}
m2=[5,6,7,8]
result= m1.union(m2)
print(result)
result= m1|m2
print(result)

# intersecotion
m1={1,2,3,4,5,6}
m2=[5,6,7,8]
result=m1.intersection(m2)
print(result)
result= m1&m2
print(result)

# isdisjoint()
m1={1,2,3,4,5,6}
m2=[5,6,7,8]
print(m2.issubset(m1)) # false
m3={4,5,6}
print(m3.issubset(m1))# true


# symmetric drifferce

m1={1,2,3,4,5,6}
m2=[5,6,7,8]

print(m1.symmetric_difference(m2))#1,2,3,4,7,8
result = m1 ^ m2
print(result)

# symmetric difference update
m1={1,2,3,4,5,6}
m2=[5,6,7,8]
m1.symmetric_difference_update(m2)
print(m1)#1,2,3,4,7,8
 



